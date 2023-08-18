# -*- coding: utf-8 -*-
import os

from googleapiclient.discovery import build


class Video:
    """Класс для видео"""

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется данными о видео"""
        self.video_id = video_id
        self.dict_of_video = self.get_service().videos().list(id=self.video_id,
                                                              part='snippet,statistics').execute()
        self.title = self.dict_of_video.get('items')[0].get('snippet').get('title')
        self.url = f"https://www.youtube.com/watch?v={video_id}"
        self.views = int(self.dict_of_video.get('items')[0].get('statistics').get('viewCount'))
        self.likes = int(self.dict_of_video.get('items')[0].get('statistics').get('likeCount'))

    def __str__(self) -> str:
        return self.title

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('y_api_kei'))


class PLVideo(Video):
    """Класс для видео в плейлисте"""

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Экземпляр инициализируется id видео и id плейлиста"""
        super().__init__(video_id)
        self.playlist_id = playlist_id
