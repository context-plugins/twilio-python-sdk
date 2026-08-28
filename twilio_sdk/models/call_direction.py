from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallDirection(SdkBaseModel):
    """Number of calls made in each direction."""

    outbound: Optional[int] = UNSET
    """Number of outbound calls"""

    inbound: Optional[int] = UNSET
    """Number of inbound calls"""


class CallDirectionDict(TypedDict):
    outbound: NotRequired[int]
    inbound: NotRequired[int]
