from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .configuration import Configuration, ConfigurationDict
from .conversations_v2_participant import ConversationsV2Participant, ConversationsV2ParticipantDict
from .enums.status3 import Status3OrStr


class ConversationsV2Conversation(SdkBaseModel):
    id: str
    """Conversation ID."""

    account_id: str = Field(alias="accountId")
    """Account ID."""

    configuration_id: str = Field(alias="configurationId")
    """Configuration ID."""

    status: Optional[Status3OrStr] = UNSET
    """Conversation status."""

    name: OptionalNullable[str] = UNSET
    """Conversation name."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp when this Conversation was created."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when this Conversation was last updated."""

    configuration: Optional[Configuration] = UNSET
    """Full configuration settings for this Conversation."""

    participants: Optional[list[ConversationsV2Participant]] = UNSET
    """Participants in this Conversation."""


class ConversationsV2ConversationDict(TypedDict):
    id: str
    account_id: str
    configuration_id: str
    status: NotRequired[Status3OrStr]
    name: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    configuration: NotRequired[Configuration | ConfigurationDict]
    participants: NotRequired[list[ConversationsV2Participant | ConversationsV2ParticipantDict]]
