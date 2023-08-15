import pytest
import json
from src.channel import Channel


@pytest.fixture
def channel():
    channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"
    return Channel(channel_id)


def test_channel_info(channel):
    assert channel.title == "MoscowPython"
    assert channel.count_podpishchikov == 26300


def test_channel_url(channel):
    assert channel.url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"


def test_channel_to_json(channel):
    channel.to_json("test_channel.json")
    with open("test_channel.json", "r") as file:
        data = json.load(file)
        assert data["title"] == "MoscowPython"
        assert data["count_podpishchikov"] == 26300
        assert data["url"] == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"


def test_print_info(channel, capsys):
    # Проверяем, что вывод информации о канале происходит без ошибок
    channel.print_info()
    captured = capsys.readouterr()
    assert captured.out != ""


def test_add():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    assert channel1 + channel2 != 100100


def test_sub():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    assert channel1 - channel2 != -48300
    assert channel2 - channel1 != 48300


def test_comparison():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    assert (channel1 > channel2) == False
    assert (channel1 >= channel2) == False
    assert (channel1 < channel2) == True
    assert (channel1 <= channel2) == True
    assert (channel1 == channel2) == False