from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel4 import Channel4OrStr


class ConversationsV2CommunicationEndpoint(SdkBaseModel):
    """Endpoint for a communication participant. Supports three resolution modes:

    1. **participantId + channel**: Resolves address from participant's registered addresses
    2. **participantId only**: Resolves when participant has exactly one address
    3. **address + channel**: Uses explicit address (for new recipients or cross-channel)"""

    participant_id: Optional[str] = Field(default=UNSET, alias="participantId")
    """Participant ID to resolve address from. When provided, Conversations looks up the participant's registered
    addresses and selects based on channel."""

    address: Optional[str] = UNSET
    """Explicit address formatted according to channel type:
    - SMS/VOICE: E.164 phone number (such as "+18005550100")
    - WHATSAPP: Phone number with whatsapp prefix (such as "whatsapp:+18005550100")
    - RCS: Sender ID or phone number with rcs prefix (such as "rcs:brand_acme_agent" or "rcs:+18005550100")
    - CHAT: Customer-defined string identifier"""

    channel: Optional[Channel4OrStr] = UNSET
    """Channel type. Required when participantId has multiple addresses or when using explicit address."""


class ConversationsV2CommunicationEndpointDict(TypedDict):
    participant_id: NotRequired[str]
    address: NotRequired[str]
    channel: NotRequired[Channel4OrStr]
