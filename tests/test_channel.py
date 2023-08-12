import pytest
import requests
import json
from src.channel import Channel


@pytest.fixture(scope="session")
def channel():
    return Channel("UC-OVMPlMA3-YCIeg4z5z23A")


def test_fetch_channel_info(channel):
    # Проверяем, что данные о канале корректно заполняются
    channel._fetch_channel_info()
    assert channel.title != ""
    assert channel.description != ""
    assert channel.url != ""
    assert channel.subscriber_count >= 0
    assert channel.video_count >= 0
    assert channel.view_count >= 0


def test_print_info(channel, capsys):
    # Проверяем, что вывод информации о канале происходит без ошибок
    channel.print_info()
    captured = capsys.readouterr()
    assert captured.out != ""


def test_to_json(channel, tmp_path):
    # Проверяем, что сохранение данных в JSON файл происходит без ошибок
    file_path = tmp_path / "channel.json"
    channel.to_json(file_path)
    assert file_path.exists()

    # Проверяем, что сохраненные данные соответствуют ожидаемым значениям
    with open(file_path) as file:
        data = json.load(file)
    assert data["channelId"] == "UC-OVMPlMA3-YCIeg4z5z23A"
    assert data["title"] == channel.title
    assert data["description"] == channel.description
    assert data["url"] == channel.url
    assert data["subscriberCount"] == channel.subscriber_count
    assert data["videoCount"] == channel.video_count
    assert data["viewCount"] == channel.view_count


def test_get_service():
    # Проверяем, что метод get_service возвращает объект requests.Session
    session = Channel.get_service()
    assert isinstance(session, requests.Session)
