from ytkit.core.get_search_videos import GetSearchVideo
from ytkit.core.get_video_subtitle import GetVideoSubtitle
from ytkit.base import BaseGet


class GetSearchSubtitle(BaseGet):
    """
    A class that combines YouTube search and subtitle fetching.
    """

    def __init__(self) -> None:
        # Instantiate the search and subtitle fetching classes
        self._get_search_videos = GetSearchVideo()
        self._get_subtitle = GetVideoSubtitle()

    def get(self, **kwargs):
        """
        Fetch subtitles for YouTube videos obtained from a search query.

        :param kwargs: Keyword arguments for search and subtitle fetching.
            - query: str or List[str] - Search query or queries.
            - limit: int - Maximum number of videos to fetch (default: 10).
            - sleep: int - Sleep time between requests (default: 1).
            - sort_by: str - Sorting method for search results (default: 'relevance').
            - results_type: str - Type of results to fetch (default: 'video').
            - language: str - Language code for subtitles (default: 'en').
            - save_to_disk: str - Folder path to save the subtitles (optional).
        :return: List[str] - A list of subtitles for the fetched videos.
        """
        search_video_ids = self._get_search_videos.get(**kwargs)
        if not search_video_ids:
            raise ValueError("No video IDs found for the given query.")

        kwargs["video_ids"] = search_video_ids
        subtitles = self._get_subtitle.get(**kwargs)

        return subtitles

        
