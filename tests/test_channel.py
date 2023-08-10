import json

import pytest
import os

import requests

from src.channel import Channel

api_key: str = os.getenv('y_api_kei')


def test_to_json(tmp_path):
    file_path = tmp_path / "channel.json"

    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel.to_json(file_path)

    expected_data = {
        "channelId": "UC-OVMPlMA3-YCIeg4z5z23A",
        "title": "",
        "description": "",
        "url": "",
        "subscriberCount": 0,
        "videoCount": 0,
        "viewCount": 0
    }

    with open(file_path, 'r') as file:
        data = json.load(file)

        assert data != expected_data


