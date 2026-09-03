from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .outbound_carrier_calling import OutboundCarrierCalling, OutboundCarrierCallingDict


class Kyt(SdkBaseModel):
    """Know Your Traffic (KYT) metrics focused on outbound carrier performance and trust signals for the report
    period."""

    outbound_carrier_calling: Optional[OutboundCarrierCalling] = UNSET
    """KYT metrics for outbound carrier calling."""


class KytDict(TypedDict):
    outbound_carrier_calling: NotRequired[OutboundCarrierCalling | OutboundCarrierCallingDict]
