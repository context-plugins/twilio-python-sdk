from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel1 import Channel1OrStr


class ConversationsV2Address(SdkBaseModel):
    channel: Channel1OrStr
    """The channel for Communication."""

    address: str
    """The address value formatted according to channel type:
    - SMS/VOICE: E.164 phone number (such as "+18005550100")
    - WHATSAPP: Phone number with whatsapp prefix (such as "whatsapp:+18005550100")
    - RCS: Sender ID or phone number with rcs prefix (such as "rcs:brand_acme_agent" or "rcs:+18005550100")
    - CHAT: Customer-defined string identifier"""

    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")
    """Channel-specific ID for correlating Communications."""


class ConversationsV2AddressDict(TypedDict):
    channel: Channel1OrStr
    address: str
    channel_id: NotRequired[str]
