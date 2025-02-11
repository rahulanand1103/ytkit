from scrapetube import get_playlist
from typing import Generator, Optional, Dict
from ytkit.core.get_playlist_videos.schema import PlaylistInput, GetPlaylistVideosError
from ytkit.base import BaseGet


class GetPlaylistVideos(BaseGet):
    """
    A class to scrape video details from a YouTube playlist.
    """

    def _fetch_videos(
        self, playlist_id: str, limit: Optional[int] = None, sleep: int = 1
    ) -> Generator[dict, None, None]:
        """
        Fetch videos from a YouTube playlist.

        :param playlist_id: str - The ID of the YouTube playlist.
        :param limit: int - The maximum number of videos to fetch (optional).
        :param sleep: int - The sleep time between requests (optional, default is 1).
        :return: Generator[dict] - A generator of video details.
        """
        # Validate inputs using Pydantic model
        validated_input = PlaylistInput(
            playlist_id=playlist_id, limit=limit, sleep=sleep
        )

        return get_playlist(
            playlist_id=validated_input.playlist_id,
            limit=validated_input.limit,
            sleep=validated_input.sleep,
        )

    def get(self, **kwargs):
        try:
            """
            Display the video IDs from the fetched videos.

            :param playlist_id: str - The ID of the YouTube playlist.
            :param limit: int - The maximum number of videos to fetch (optional).
            :param sleep: int - The sleep time between requests (optional, default is 1).
            """
            validated_input = PlaylistInput(**kwargs)
            videos = self._fetch_videos(
                playlist_id=validated_input.playlist_id,
                limit=validated_input.limit,
                sleep=validated_input.sleep,
            )
            videos_list = [video["videoId"] for video in videos]
            if len(videos_list) == 0:
                raise GetPlaylistVideosError(
                    "Unable to fetch playlist videos. Please verify the `playlist_id`."
                )
            return videos_list
        except Exception as e:
            raise GetPlaylistVideosError(
                f"Unable to fetch playlist videos. Please verify the `playlist_id`.Error: {str(e)}"
            )
