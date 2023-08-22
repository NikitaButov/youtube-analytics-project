import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build


class PlayList:
    """Класс для плейлиста"""

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста."""
        self.__playlist_id = playlist_id
        self.dict_of_playlist = self.get_service().playlists().list(id=self.__playlist_id, part='snippet').execute()
        self.title = self.dict_of_playlist.get('items')[0].get('snippet').get('title')
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.videos = []

    @property
    def playlist_id(self):
        return self.__playlist_id

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('y_api_kei'))

    def get_videos_from_playlist(self):
        videos = []
        next_page_token = None
        while True:
            playlist_items = self.get_service().playlistItems().list(playlistId=self.__playlist_id, part='snippet',
                                                                     maxResults=50, pageToken=next_page_token).execute()
            for item in playlist_items.get('items', []):
                videos.append(item['snippet']['resourceId']['videoId'])
            next_page_token = playlist_items.get('nextPageToken')
            if not next_page_token:
                break
        self.videos = videos
        return videos

    def total_duration(self):
        """Возвращает суммарную длительность плейлиста"""
        if not self.videos:
            self.get_videos_from_playlist()
        duration = timedelta()
        for video in self.videos:
            video_duration = self.get_service().videos().list(id=video, part='contentDetails',
                                                              fields='items/contentDetails/duration').execute()
            duration_string = video_duration['items'][0]['contentDetails']['duration']
            parsed_duration = self.parse_duration(duration_string)
            duration += parsed_duration
        return duration

    def parse_duration(self, duration):
        """Вспомогательный метод для преобразования строкового представления длительности видео в объект timedelta"""
        if not duration:
            return timedelta()

        try:
            total_seconds = 0
            for time in duration.split('T')[1:]:
                if 'H' in time:
                    hours = int(time.split('H')[0])
                    total_seconds += hours * 3600
                    time = time.split('H')[1]
                if 'M' in time:
                    minutes = int(time.split('M')[0])
                    total_seconds += minutes * 60
                    time = time.split('M')[1]
                if 'S' in time:
                    seconds = int(time.split('S')[0])
                    total_seconds += seconds
        except:
            return timedelta()

        return timedelta(seconds=total_seconds)

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        videos = self.get_videos_from_playlist()

        best_video = ''
        max_likes = 0
        for video_id in videos:
            video_likes = self.get_service().videos().list(id=video_id, part='statistics',
                                                           fields='items/statistics(likeCount)').execute()
            likes = int(video_likes['items'][0]['statistics'].get('likeCount', 0))
            if likes > max_likes:
                max_likes = likes
                best_video = f"https://youtu.be/{video_id}"
        return best_video
