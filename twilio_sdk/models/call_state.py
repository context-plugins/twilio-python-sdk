from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallState(SdkBaseModel):
    """Number of calls made in each state."""

    completed: Optional[int] = UNSET
    """Number of completed calls"""

    fail: Optional[int] = UNSET
    """Number of failed calls"""

    busy: Optional[int] = UNSET
    """Number of busy calls"""

    noanswer: Optional[int] = UNSET
    """Number of no-answer calls"""

    canceled: Optional[int] = UNSET
    """Number of canceled calls"""


class CallStateDict(TypedDict):
    completed: NotRequired[int]
    fail: NotRequired[int]
    busy: NotRequired[int]
    noanswer: NotRequired[int]
    canceled: NotRequired[int]
