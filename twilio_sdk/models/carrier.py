from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Carrier(SdkBaseModel):
    carrier: Optional[str] = UNSET
    """The name of the carrier."""

    total_calls: Optional[int] = UNSET
    """Total number of outbound calls for the carrier in the country."""

    blocked_calls: Optional[int] = UNSET
    """Total number of blocked outbound calls for the carrier in the country."""

    blocked_calls_percentage: Optional[float] = UNSET
    """Percentage of blocked outbound calls for the carrier in the country."""


class CarrierDict(TypedDict):
    carrier: NotRequired[str]
    total_calls: NotRequired[int]
    blocked_calls: NotRequired[int]
    blocked_calls_percentage: NotRequired[float]
