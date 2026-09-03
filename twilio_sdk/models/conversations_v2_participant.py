from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .conversations_v2_address import ConversationsV2Address, ConversationsV2AddressDict
from .enums.type2 import Type2OrStr


class ConversationsV2Participant(SdkBaseModel):
    id: str
    """Participant ID."""

    conversation_id: str = Field(alias="conversationId")
    """Conversation ID."""

    account_id: str = Field(alias="accountId")
    """Account ID."""

    name: str
    """Participant display name."""

    type_: Optional[Type2OrStr] = Field(default=UNSET, alias="type")
    """Type of Participant in the Conversation."""

    profile_id: Optional[str] = Field(default=UNSET, alias="profileId")
    """Profile ID. Note: This field is only resolved for ``CUSTOMER`` participant types, not for ``HUMAN_AGENT`` or
    ``AI_AGENT`` participants."""

    addresses: Optional[list[ConversationsV2Address]] = UNSET
    """Communication addresses for this Participant. Address format varies by channel:
    - SMS/VOICE: E.164 phone number (such as "+18005550100")
    - EMAIL: Email address (such as "user@example.com")
    - WHATSAPP: Phone number with whatsapp prefix (such as "whatsapp:+18005550100")
    - RCS: Sender ID or phone number with rcs prefix (such as "rcs:brand_acme_agent" or "rcs:+18005550100")"""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp when this Participant was created."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when this Participant was last updated."""


class ConversationsV2ParticipantDict(TypedDict):
    id: str
    conversation_id: str
    account_id: str
    name: str
    type_: NotRequired[Type2OrStr]
    profile_id: NotRequired[str]
    addresses: NotRequired[list[ConversationsV2Address | ConversationsV2AddressDict]]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
