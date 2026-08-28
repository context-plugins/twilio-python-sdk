from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LastTokenReceivedEvent(SdkBaseModel):
    total_tokens: Optional[int] = UNSET
    """Total number of tokens received."""

    total_words: Optional[int] = UNSET
    """Total number of words received."""


class LastTokenReceivedEventDict(TypedDict):
    total_tokens: NotRequired[int]
    total_words: NotRequired[int]
