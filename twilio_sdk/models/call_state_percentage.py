from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallStatePercentage(SdkBaseModel):
    """Percentage of calls made in each state."""

    completed: Optional[float] = UNSET
    """Percentage of completed inbound calls."""

    fail: Optional[float] = UNSET
    """Percentage of failed inbound calls."""

    busy: Optional[float] = UNSET
    """Percentage of busy inbound calls."""

    noanswer: Optional[float] = UNSET
    """Percentage of no-answer inbound calls."""

    canceled: Optional[float] = UNSET
    """Percentage of canceled inbound calls."""


class CallStatePercentageDict(TypedDict):
    completed: NotRequired[float]
    fail: NotRequired[float]
    busy: NotRequired[float]
    noanswer: NotRequired[float]
    canceled: NotRequired[float]
