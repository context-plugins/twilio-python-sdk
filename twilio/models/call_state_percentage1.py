from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallStatePercentage1(SdkBaseModel):
    """Percentage of calls made in each state."""

    completed: Optional[float] = UNSET
    """Percentage of completed outbound calls."""

    fail: Optional[float] = UNSET
    """Percentage of failed outbound calls."""

    busy: Optional[float] = UNSET
    """Percentage of busy outbound calls."""

    noanswer: Optional[float] = UNSET
    """Percentage of no-answer outbound calls."""

    canceled: Optional[float] = UNSET
    """Percentage of canceled outbound calls."""


class CallStatePercentage1Dict(TypedDict):
    completed: NotRequired[float]
    fail: NotRequired[float]
    busy: NotRequired[float]
    noanswer: NotRequired[float]
    canceled: NotRequired[float]
