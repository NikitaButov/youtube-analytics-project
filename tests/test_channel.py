import pytest
import requests
import json
from src.channel import Channel


@pytest.fixture(scope="session")
def channel():
    return Channel("UC-OVMPlMA3-YCIeg4z5z23A")


def test_fetch_channel_info(channel):
    # ���������, ��� ������ � ������ ��������� �����������
    channel._fetch_channel_info()
    assert channel.title != ""
    assert channel.description != ""
    assert channel.url != ""
    assert channel.subscriber_count >= 0
    assert channel.video_count >= 0
    assert channel.view_count >= 0


def test_print_info(channel, capsys):
    # ���������, ��� ����� ���������� � ������ ���������� ��� ������
    channel.print_info()
    captured = capsys.readouterr()
    assert captured.out != ""


def test_to_json(channel, tmp_path):
    # ���������, ��� ���������� ������ � JSON ���� ���������� ��� ������
    file_path = tmp_path / "channel.json"
    channel.to_json(file_path)
    assert file_path.exists()

    # ���������, ��� ����������� ������ ������������� ��������� ���������
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
    # ���������, ��� ����� get_service ���������� ������ requests.Session
    session = Channel.get_service()
    assert isinstance(session, requests.Session)
