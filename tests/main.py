import pytest
from ytkit import (
    GetChannelSubtitle,
    GetPlaylistSubtitle,
    GetSearchSubtitle,
    GetVideoSubtitle,
)


def test_get_playlist_subtitle():
    get_playlist_subtlte = GetPlaylistSubtitle()
    result = get_playlist_subtlte.get(
        playlist_id="PL8dPuuaLjXtNamNKW5qlS-nKgA0on7Qze",
        language="en",
        save_to_disk="playlist_data",
        limit=2,
    )
    assert len(result) > 0, "Expected subtitle data to be returned for the playlist"


def test_get_channel_subtitle():
    get_channel_subtlte = GetChannelSubtitle()
    result = get_channel_subtlte.get(
        channel_username="TEDx",
        sort_by="popular",
        limit=2,
        save_to_disk="channel_data",
        language="en",
    )
    assert len(result) > 0, "Expected subtitle data to be returned for the channel"


def test_get_search_subtitle():
    get_search_subtlte = GetSearchSubtitle()
    result = get_search_subtlte.get(
        query="python tutorial", save_to_disk="search_data", limit=2
    )
    assert len(result) > 0, "Expected subtitle data to be returned for the search query"


def test_get_video_subtitle():
    get_video_subtitle = GetVideoSubtitle()
    result = get_video_subtitle.get(
        video_ids=["_uQrJ0TkZlc"],
        language="en",
        save_to_disk="individual_video",
    )
    assert len(result) > 0, "Expected subtitle data to be returned for the video"
