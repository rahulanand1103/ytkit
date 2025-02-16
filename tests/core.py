import pytest
from ytkit import (
    GetChannelVideos,
    GetPlaylistVideos,
    GetSearchVideo,
)

@pytest.fixture
def channel_video():
    return GetChannelVideos()

@pytest.fixture
def playlist_video():
    return GetPlaylistVideos()

@pytest.fixture
def search_video():
    return GetSearchVideo()


def test_get_channel_videos(channel_video):
    result = channel_video.get(channel_url="https://www.youtube.com/@TEDx",
                                limit=2,
                                language="en")
    assert len(result) > 0, "Expected result length to be greater than 0"

def test_get_channel_username(channel_video):
    result = channel_video.get(channel_username="TEDx",
                                sort_by="popular",
                                limit=2,
                                language="en")
    assert len(result) > 0, "Expected result length to be greater than 0"

def test_get_playlist_videos(playlist_video):
    result = playlist_video.get(playlist_id="PL8dPuuaLjXtNamNKW5qlS-nKgA0on7Qze")
    assert len(result) > 0, "Expected result length to be greater than 0"

def test_get_search_video(search_video):
    result = search_video.get(query="python")
    assert len(result) > 0, "Expected result length to be greater than 0"
