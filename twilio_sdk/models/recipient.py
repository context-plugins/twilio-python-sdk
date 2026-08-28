from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel11 import Channel11OrStr
from .enums.delivery_status import DeliveryStatusOrStr


class Recipient(SdkBaseModel):
    address: str
    """The address value formatted according to channel type:
    - SMS/VOICE: E.164 phone number (such as "+18005550100")
    - WHATSAPP: Phone number with whatsapp prefix (such as "whatsapp:+18005550100")
    - RCS: Sender ID or phone number with rcs prefix (such as "rcs:brand_acme_agent" or "rcs:+18005550100")
    - CHAT: Customer-defined string identifier"""

    channel: Channel11OrStr
    """Channel type for the Participant address."""

    participant_id: Optional[str] = Field(default=UNSET, alias="participantId")
    """Participant ID associated with this address."""

    delivery_status: Optional[DeliveryStatusOrStr] = Field(default=UNSET, alias="deliveryStatus")
    """Delivery status of the Communication to this recipient."""


class RecipientDict(TypedDict):
    address: str
    channel: Channel11OrStr
    participant_id: NotRequired[str]
    delivery_status: NotRequired[DeliveryStatusOrStr]
