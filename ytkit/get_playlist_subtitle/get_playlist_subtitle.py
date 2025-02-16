from ytkit.core.get_playlist_videos import GetPlaylistVideos
from ytkit.core.get_video_subtitle import GetVideoSubtitle
from ytkit.base import BaseGet


class GetPlaylistSubtitle(BaseGet):
    def __init__(self) -> None:
        self._get_playlist_videos = GetPlaylistVideos()
        self._get_subtitle = GetVideoSubtitle()

    def get(self, **kwargs):
        """
        Retrieve subtitles for all videos in a YouTube playlist.

        :param playlist_id: str - The ID of the YouTube playlist
        :param limit: int - Maximum number of videos to fetch from the playlist (optional)
        :param sleep: int - Sleep time between requests to fetch videos (optional, default is 1)
        :param language: str - Desired language code for subtitles (default: 'en')
        :param save_to_disk: str - Folder path to save the subtitles (optional, default is None)
        :return: List[dict] - A list of subtitle data for each video in the playlist
        """
        playlist_video_ids = self._get_playlist_videos.get(**kwargs)
        kwargs["video_ids"] = playlist_video_ids
        return self._get_subtitle.get(**kwargs)
