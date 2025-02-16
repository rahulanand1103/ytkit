# ytkit 📺

With **ytkit**, you can fetch subtitles from entire YouTube channels, playlists, and search results in just a few lines of code! Perfect for RAG, AI applications, and content analysis.

## Installation

Install via pip:

```sh
pip install ytkit
```

Upgrade to the latest version:

```sh
pip install --upgrade ytkit
```

## Requirements

*   Python 3.7+


## Usage

### GetChannelSubtitle

Fetch subtitles from all videos in a YouTube channel.

```python
from ytkit import GetChannelSubtitle

get_channel_subtitle = GetChannelSubtitle()
result = get_channel_subtitle.get(
    channel_username="TEDx",
    limit=2,
    language="en",
    save_to_disk="channel_data"
)
```

### GetPlaylistSubtitle

Fetch subtitles from all videos in a YouTube playlist.

```python
from ytkit import GetPlaylistSubtitle

get_playlist_subtitle = GetPlaylistSubtitle()
result = get_playlist_subtitle.get(
    playlist_id="PL8dPuuaLjXtNamNKW5qlS-nKgA0on7Qze",
    limit=2,
    language="en",
    save_to_disk="data"
)
```

### GetSearchSubtitle

Fetch subtitles for videos based on a search query.

```python
from ytkit import GetSearchSubtitle

get_search_subtitle = GetSearchSubtitle()
result = get_search_subtitle.get(
    query="python tutorial",
    limit=2,
    language="en",
    save_to_disk="test"
)
```

### GetVideoSubtitle

Fetch subtitles for specific YouTube videos.

```python
from ytkit import GetVideoSubtitle

get_video_subtitle = GetVideoSubtitle()
result = get_video_subtitle.get(
    video_ids=["_uQrJ0TkZlc"],
    language="en",
    save_to_disk="subtitles"
)
```
🚀 **ytkit** simplifies subtitle extraction for YouTube videos!


## Acknowledgements

This project leverages the power of two incredible open-source libraries: 

- `scrapetube` (>=2.5.1, <3.0.0): A simple yet effective Python library for scraping YouTube channels and playlists. It made fetching video metadata seamless and efficient.

- `youtube-transcript-api` (>=0.6.3, <0.7.0): This library provided a straightforward way to retrieve YouTube video transcripts, enabling automatic extraction of subtitles without requiring YouTube API keys.

A huge thanks to the developers and maintainers of these projects for their contributions to the open-source community!

If you find this project helpful, please consider checking out these libraries and giving them a star on GitHub.


