from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class Word(SdkBaseModel):
    text: str
    """The transcribed word."""

    start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startTime")
    """Start timestamp of this word."""

    end_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endTime")
    """End timestamp of this word."""


class WordDict(TypedDict):
    text: str
    start_time: NotRequired[RFC3339DateTime]
    end_time: NotRequired[RFC3339DateTime]
