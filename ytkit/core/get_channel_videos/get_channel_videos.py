from scrapetube import get_channel
from ytkit.core.get_channel_videos.schema import ChannelInput, GetChannelVideosError
from ytkit.base import BaseGet
from typing import Generator


class GetChannelVideos(BaseGet):
    """
    A class to scrape video details from a YouTube channel using dynamic inputs.
    """

    def _fetch_videos(self, **kwargs) -> Generator[dict, None, None]:
        """
        Fetch videos from a YouTube channel with dynamic inputs.
        """
        # Validate inputs using Pydantic model
        validated_input = ChannelInput(**kwargs)

        return get_channel(
            channel_id=validated_input.channel_id,
            channel_url=validated_input.channel_url,
            channel_username=validated_input.channel_username,
            limit=validated_input.limit,
            sleep=validated_input.sleep,
            sort_by=validated_input.sort_by,
            content_type=validated_input.content_type,
        )

    def get(self, **kwargs):
        """
        Retrieve and return the video IDs from the fetched videos.

        :param channel_id: str (optional) - The unique ID of the YouTube channel.
        :param channel_url: str (optional) - The URL of the YouTube channel.
        :param channel_username: str (optional) - The username of the YouTube channel.
        :param limit: int (optional) - The maximum number of videos to fetch.
        :param sleep: float (optional) - The sleep time between requests (default is 1).
        :param sort_by: str (optional) - The sorting order of videos ("newest", "oldest", "popular", default is "newest").
        :param content_type: str (optional) - The type of content to fetch ("videos", "shorts", "streams", default is "videos").

        :return: List[str] - A list of video IDs.

        :raises GetChannelVideosError: If an error occurs while fetching videos.
        """
        try:
            videos = self._fetch_videos(**kwargs)
            videos_list = [video["videoId"] for video in videos]
            return videos_list
        except Exception as e:
            raise GetChannelVideosError(
                f"Unable to fetch channel videos. Please verify the `channel_id`, `channel_url`, or `channel_username`. Error: {str(e)}"
            )
