from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.end_status import EndStatusOrStr


class CallWrapUpEvent(SdkBaseModel):
    duration_in_seconds: Optional[int] = UNSET
    """Duration in seconds."""

    end_status: Optional[EndStatusOrStr] = UNSET
    """End status of the call wrap up event."""


class CallWrapUpEventDict(TypedDict):
    duration_in_seconds: NotRequired[int]
    end_status: NotRequired[EndStatusOrStr]
