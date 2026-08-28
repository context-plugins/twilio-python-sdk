from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Sdk(SdkBaseModel):
    """Network issues of calls for client type. This is indicative of local network issues."""

    ice_failures_percentage: Optional[float] = UNSET
    """Percentage of ICE connection failure tag that ICE candidates have failed to find compatible connection."""

    high_latency_percentage: Optional[float] = UNSET
    """Percentage of calls with high latency."""

    high_packet_loss_percentage: Optional[float] = UNSET
    """Percentage of calls with high packet loss."""

    high_jitter_percentage: Optional[float] = UNSET
    """Percentage of calls with high jitter."""


class SdkDict(TypedDict):
    ice_failures_percentage: NotRequired[float]
    high_latency_percentage: NotRequired[float]
    high_packet_loss_percentage: NotRequired[float]
    high_jitter_percentage: NotRequired[float]
