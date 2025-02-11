from typing import Literal, Generator, List, Union
from pydantic import ValidationError
from ytkit.core.get_search_videos.schema import SearchInput, GetSearchVideoError
from scrapetube import get_search
from ytkit.base import BaseGet


class GetSearchVideo(BaseGet):
    """
    A class to scrape video details from YouTube search results using dynamic inputs.
    """

    def _fetch_videos(
        self,
        query: Union[str, List[str]],
        limit: int = 10,
        sleep: int = 1,
        sort_by: Literal[
            "relevance", "upload_date", "view_count", "rating"
        ] = "relevance",
        results_type: Literal["video", "channel", "playlist", "movie"] = "video",
    ) -> Generator[dict, None, None]:
        """
        Fetch videos from YouTube search results with dynamic inputs.

        :param query: Union[str, List[str]] - The search query or list of queries.
        :param limit: int - The maximum number of results to fetch (default: 10).
        :param sleep: int - The sleep time between requests.
        :param sort_by: Literal - The sorting order of results.
        :param results_type: Literal - The type of results to fetch (e.g., videos, channels).
        :return: Generator[dict] - A generator of video details.
        """
        # Validate inputs using the SearchInput model
        validated_input = SearchInput(
            query=query,
            limit=limit,
            sleep=sleep,
            sort_by=sort_by,
            results_type=results_type,
        )

        for single_query in validated_input.query:
            yield from get_search(
                query=single_query,
                limit=validated_input.limit,
                sleep=validated_input.sleep,
                sort_by=validated_input.sort_by,
                results_type=validated_input.results_type,
            )

    def get(self, **kwargs) -> List[str]:
        """
        Fetch and return the video IDs from the YouTube search results.

        :param kwargs: Keyword arguments to pass to the `fetch_videos` method.
        :return: list[str] - A list of video IDs.
        """
        try:
            # Validate inputs using the SearchInput model
            validated_input = SearchInput(**kwargs)

            videos = self._fetch_videos(
                query=validated_input.query,
                limit=validated_input.limit,
                sleep=validated_input.sleep,
                sort_by=validated_input.sort_by,
                results_type=validated_input.results_type,
            )
            videosids = [video["videoId"] for video in videos]

            return videosids
        except Exception as e:
            raise GetSearchVideoError(
                f"something went wrong while searching. Error: {str(e)}"
            )
