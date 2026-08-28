from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.messaging_v2_rcs_carrier_status import MessagingV2RcsCarrierStatusOrStr


class MessagingV2RcsCarrier(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the carrier. For example, ``Verizon`` or ``AT&T`` for US."""

    status: Optional[MessagingV2RcsCarrierStatusOrStr] = UNSET
    """The carrier-level status."""


class MessagingV2RcsCarrierDict(TypedDict):
    name: NotRequired[str]
    status: NotRequired[MessagingV2RcsCarrierStatusOrStr]
