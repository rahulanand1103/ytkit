from typing import List, Union
from pydantic import BaseModel, Field
import os


class SubtitleInput(BaseModel):
    video_ids: List[str] = Field(..., description="List of YouTube video IDs")
    language: str = Field("en", description="Desired language code for subtitles")
    save_to_disk: Union[None, str] = Field(
        None, description="Folder path to save the transcript files"
    )

    @classmethod
    def validate_video_ids(cls, video_ids: Union[str, List[str]]) -> List[str]:
        """
        Convert a single string video_id to a list for consistent handling.

        :param video_ids: str or List[str] - Single video ID or list of IDs
        :return: List[str] - List of video IDs
        """
        if isinstance(video_ids, str):
            return [video_ids]
        return video_ids
