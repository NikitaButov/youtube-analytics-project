# -*- coding: utf-8 -*-
from src.video import Video, PLVideo


def test_get_service():
    service = Video.get_service()
    assert service is not None


def test_video():
    video_id = 'AWX4JnAnjBE'
    video = Video(video_id)
    assert video.video_id == video_id
    assert video.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video.url == f"https://www.youtube.com/watch?v={video_id}"
    assert video.views != 1000
    assert video.likes != 500


def test_plvideo():
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert video2.playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert video2.title == 'MoscowPython Meetup 78 - вступление'
    assert video2.url == f"https://www.youtube.com/watch?v=4fObz_qw9u4"
    assert video2.views != 1000
    assert video2.likes != 500

def test_broken_video():
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.likes is None
    assert broken_video.url is None
    assert broken_video.views is None