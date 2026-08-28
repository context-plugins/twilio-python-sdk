from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TwilioGateway(SdkBaseModel):
    """Network related metrics for Twilio Gateway calls only."""

    high_latency_percentage: Optional[float] = UNSET
    """Percentage of calls with high latency."""

    high_packet_loss_percentage: Optional[float] = UNSET
    """Percentage of calls with high packet loss."""

    high_jitter_percentage: Optional[float] = UNSET
    """Percentage of calls with high jitter."""


class TwilioGatewayDict(TypedDict):
    high_latency_percentage: NotRequired[float]
    high_packet_loss_percentage: NotRequired[float]
    high_jitter_percentage: NotRequired[float]
