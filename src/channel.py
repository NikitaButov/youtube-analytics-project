import os
import requests
import json

api_key: str = os.getenv('y_api_kei')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={self.channel_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        print(json.dumps(data, indent=2, ensure_ascii=False))
