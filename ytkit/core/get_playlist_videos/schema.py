from typing import Generator, Optional, Dict, List
from pydantic import BaseModel, Field
from dataclasses import dataclass


class PlaylistInput(BaseModel):
    playlist_id: str = Field(..., description="The ID of the YouTube playlist")
    limit: Optional[int] = None
    sleep: int = Field(
        1, ge=0, description="Sleep time between requests (default is 1)"
    )


class GetPlaylistVideosError(Exception):
    """Exception for GetPlaylistVideos Error errors."""
    pass
