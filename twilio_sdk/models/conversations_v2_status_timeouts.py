from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsV2StatusTimeouts(SdkBaseModel):
    """Timeout settings for channel status transitions."""

    inactive: Optional[int] = UNSET
    """Inactivity timeout in minutes."""

    closed: Optional[int] = UNSET
    """Close timeout in minutes."""


class ConversationsV2StatusTimeoutsDict(TypedDict):
    inactive: NotRequired[int]
    closed: NotRequired[int]
