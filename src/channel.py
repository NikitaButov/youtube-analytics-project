import os
import requests
import json

api_key: str = os.getenv('y_api_kei')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ""
        self.description = ""
        self.url = ""
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0

        self._fetch_channel_info()

    def _fetch_channel_info(self) -> None:
        """Заполняет атрибуты экземпляра данными о канале."""
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        try:
            channel_info = data["items"][0]
        except KeyError:
            raise KeyError('Ошибка при получении данных о канале')
        self.title = channel_info["snippet"]["title"]
        self.description = channel_info["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(channel_info["statistics"]["subscriberCount"])
        self.video_count = int(channel_info["statistics"]["videoCount"])
        self.view_count = int(channel_info["statistics"]["viewCount"])

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return requests.Session()

    def to_json(self, file_path: str) -> None:
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON."""
        data = {
            "channelId": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriber_count,
            "videoCount": self.video_count,
            "viewCount": self.view_count
        }

        with open(file_path, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
