import pytest

from src.channel import Channel


@pytest.fixture
def channel():
    channel_id = "1"
    return Channel(channel_id)


def test_print_info(channel):
    channel.__init__("UC-OVMPlMA3-YCIeg4z5z23A")
    channel.print_info()
