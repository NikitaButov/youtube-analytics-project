import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.dict_of_channel = self.get_service().channels().list(id=self.channel_id,
                                                                  part='snippet,statistics').execute()  # id канала
        self.title = self.dict_of_channel.get('items')[0].get('snippet').get('title')  # название канала
        self.description = self.dict_of_channel.get('items')[0].get('snippet').get('description')  # описание канала
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"  # ссылка на канал
        self.count_podpishchikov = int(
            self.dict_of_channel.get('items')[0].get('statistics').get('subscriberCount'))  # количество подписчиков
        self.video_count = int(
            self.dict_of_channel.get('items')[0].get('statistics').get('videoCount'))  # количество видео
        self.count_views = int(
            self.dict_of_channel.get('items')[0].get('statistics').get('viewCount'))  # общее количество просмотров

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Сумма подписчиков двух каналов"""
        return self.count_podpishchikov + other.count_podpishchikov

    def __sub__(self, other):
        """Разность подписчиков двух каналов"""
        return self.count_podpishchikov - other.count_podpishchikov

    def __lt__(self, other):
        """Сравнение двух каналов: меньше"""
        return self.count_podpishchikov < other.count_podpishchikov

    def __le__(self, other):
        """Сравнение двух каналов: меньше или равно"""
        return self.count_podpishchikov <= other.count_podpishchikov

    def __gt__(self, other):
        """Сравнение двух каналов: больше"""
        return self.count_podpishchikov > other.count_podpishchikov

    def __ge__(self, other):
        """Сравнение двух каналов: больше или равно"""
        return self.count_podpishchikov >= other.count_podpishchikov

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('y_api_kei'))

    @staticmethod
    def __printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.__printj(self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute())

    def to_json(self, filename):
        channel_info = {"title": self.title,
                        "channel_id": self.channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_podpishchikov": self.count_podpishchikov,
                        "video_count": self.video_count,
                        "count_views": self.count_views}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
