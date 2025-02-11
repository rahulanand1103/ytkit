from typing import Literal, Generator, Optional, List, Union
from pydantic import BaseModel, Field, ValidationError, field_validator
from dataclasses import dataclass


class SearchInput(BaseModel):
    """
    A model for validating search inputs for YouTube video scraping.
    """

    query: Union[str, List[str]] = Field(
        ..., description="The search query string or list of query strings."
    )
    limit: int = Field(
        10, ge=1, description="The maximum number of results to fetch. Default is 10."
    )
    sleep: int = Field(
        1, ge=0, description="Time in seconds to sleep between requests."
    )
    sort_by: Literal["relevance", "upload_date", "view_count", "rating"] = Field(
        "relevance", description="The sorting order of results."
    )
    results_type: Literal["video", "channel", "playlist", "movie"] = Field(
        "video", description="The type of results to fetch."
    )

    @field_validator("query")
    def validate_query(cls, value: Union[str, List[str]]):
        if isinstance(value, str) and not value.strip():
            raise ValueError("The search query must not be empty.")
        if isinstance(value, list) and not all(value):
            raise ValueError("The search query list contains empty strings.")
        # Convert single string to list for consistent handling
        if isinstance(value, str):
            return [value]
        return value


class GetSearchVideoError(Exception):
    """Exception for GetSearchVideo errors."""

    pass
