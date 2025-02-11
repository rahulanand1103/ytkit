from typing import Literal, Generator, Optional, List
from pydantic import BaseModel, Field
from dataclasses import dataclass


class ChannelInput(BaseModel):
    channel_id: Optional[str] = None
    channel_url: Optional[str] = None
    channel_username: Optional[str] = None
    limit: Optional[int] = None
    sleep: float = Field(1, ge=0)  # Ensures sleep is non-negative
    sort_by: Literal["newest", "oldest", "popular"] = "newest"
    content_type: Literal["videos", "shorts", "streams"] = "videos"

    def __init__(self, **data):
        super().__init__(**data)
        if not any([self.channel_id, self.channel_url, self.channel_username]):
            raise ValueError(
                "At least one of channel_id, channel_url, or channel_username must be provided"
            )


class GetChannelVideosError(Exception):
    """Exception for GetChannelVideosError errors."""

    pass
