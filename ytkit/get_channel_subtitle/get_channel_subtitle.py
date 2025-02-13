from ytkit.core.get_channel_videos import GetChannelVideos
from ytkit.core.get_video_subtitle import GetVideoSubtitle
from ytkit.base import BaseGet


class GetChannelSubtitle(BaseGet):
    def __init__(self) -> None:
        self._get_channel_videos = GetChannelVideos()
        self._get_subtitle = GetVideoSubtitle()

    def get(self, **kwargs):
        """
        Retrieve subtitles for all videos in a YouTube channel.

        :param channel_identifier: str - The YouTube channel ID, URL, or username
        :param limit: int - Maximum number of videos to fetch (default is no limit)
        :param sort_by: str - Sorting order of videos: 'newest', 'oldest', or 'popular'
        :param content_type: str - Type of content: 'videos', 'shorts', or 'streams'
        :param language: str - Language code for the subtitles (default: 'en')
        :param save_to_disk: str - Path to save subtitles on disk (default: None)
        :return: List[Dict[str, Any]] - A list of subtitle data for each video
        """
        channel_video_ids = self._get_channel_videos.get(**kwargs)
        # print(channel_video_id)
        kwargs["video_ids"] = channel_video_ids
        return self._get_subtitle.get(**kwargs)
