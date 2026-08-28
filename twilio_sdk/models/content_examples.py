from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ContentExamples(SdkBaseModel):
    """Content examples for the application."""

    examples: Optional[list[str]] = UNSET


class ContentExamplesDict(TypedDict):
    examples: NotRequired[list[str]]
