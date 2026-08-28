from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v2_send_message_content import (
    ConversationsV2SendMessageContent,
    ConversationsV2SendMessageContentDict,
)
from .conversations_v2_send_message_participant import (
    ConversationsV2SendMessageParticipant,
    ConversationsV2SendMessageParticipantDict,
)


class ConversationsV2SendMessagePayload(SdkBaseModel):
    from_: ConversationsV2SendMessageParticipant = Field(alias="from")
    """Identifies a participant for an Action. Supports three resolution modes:
    1. participantId + channel: Resolves address from participant's registered addresses
    2. participantId only: Resolves when participant has exactly one address
    3. address + channel: Uses explicit address"""

    to: list[ConversationsV2SendMessageParticipant]
    """The recipients of this action."""

    content: ConversationsV2SendMessageContent
    """Content for a SEND_MESSAGE action."""

    channel_settings: Optional[Any] = Field(default=UNSET, alias="channelSettings")
    """Channel-specific parameters forwarded as-is to the downstream sending service. Allows passing backend-specific
    fields without requiring API changes."""


class ConversationsV2SendMessagePayloadDict(TypedDict):
    from_: ConversationsV2SendMessageParticipant | ConversationsV2SendMessageParticipantDict
    to: list[ConversationsV2SendMessageParticipant | ConversationsV2SendMessageParticipantDict]
    content: ConversationsV2SendMessageContent | ConversationsV2SendMessageContentDict
    channel_settings: NotRequired[Any]
