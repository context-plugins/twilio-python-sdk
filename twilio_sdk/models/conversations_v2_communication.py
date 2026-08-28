from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .conversations_v2_participant_address import (
    ConversationsV2ParticipantAddress,
    ConversationsV2ParticipantAddressDict,
)
from .recipient import Recipient, RecipientDict
from .unions.content import Content, ContentDict


class ConversationsV2Communication(SdkBaseModel):
    id: str
    """Communication ID."""

    conversation_id: str = Field(alias="conversationId")
    """Conversation ID."""

    account_id: str = Field(alias="accountId")
    """Account ID."""

    author: ConversationsV2ParticipantAddress
    content: Content
    """The content of the Communication using type field for discrimination."""

    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")
    """Channel-specific reference ID."""

    resource_id: Optional[str] = Field(default=UNSET, alias="resourceId")
    """External resource identifier for this Communication (e.g. MessageSid for SMS/RCS/WhatsApp, TranscriptionSid +
    MessageIndex for Voice). When set, used for Communication deduplication/uniqueness within a Conversation."""

    recipients: list[Recipient]
    """Communication recipients."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp when this Communication was created."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when this Communication was last updated."""

    occurred_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="occurredAt")
    """ISO 8601 timestamp when the communication occurred."""


class ConversationsV2CommunicationDict(TypedDict):
    id: str
    conversation_id: str
    account_id: str
    author: ConversationsV2ParticipantAddress | ConversationsV2ParticipantAddressDict
    content: Content | ContentDict
    channel_id: NotRequired[str]
    resource_id: NotRequired[str]
    recipients: list[Recipient | RecipientDict]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    occurred_at: NotRequired[RFC3339DateTime]
