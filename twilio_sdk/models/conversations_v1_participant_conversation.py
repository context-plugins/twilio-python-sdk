from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.participant_conversation_enum_state import ParticipantConversationEnumStateOrStr


class ConversationsV1ParticipantConversation(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    conversation."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__
    this conversation belongs to."""

    participant_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Participant
    <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__."""

    participant_user_sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the conversation participant as `Conversation User
    <https://www.twilio.com/docs/conversations/api/user-resource>`__."""

    participant_identity: OptionalNullable[str] = UNSET
    """A unique string identifier for the conversation participant as `Conversation User
    <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and only if) the
    participant is using the Conversations SDK to communicate. Limited to 256 characters."""

    participant_messaging_binding: OptionalNullable[Any] = UNSET
    """Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of
    type and address fields of the participant."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ this
    Participant belongs to."""

    conversation_unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the Conversation resource."""

    conversation_friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this conversation, limited to 256 characters. Optional."""

    conversation_attributes: OptionalNullable[str] = UNSET
    """An optional string metadata field you can use to store any data you wish. The string value must contain
    structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned."""

    conversation_date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this conversation was created, given in ISO 8601 format."""

    conversation_date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this conversation was last updated, given in ISO 8601 format."""

    conversation_created_by: OptionalNullable[str] = UNSET
    """Identity of the creator of this Conversation."""

    conversation_state: Optional[ParticipantConversationEnumStateOrStr] = UNSET
    """The current state of this User Conversation. One of ``inactive``, ``active`` or ``closed``."""

    conversation_timers: OptionalNullable[Any] = UNSET
    """Timer date values representing state update for this conversation."""

    links: OptionalNullable[Any] = UNSET
    """Contains absolute URLs to access the `participant
    <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ and `conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ of this conversation."""


class ConversationsV1ParticipantConversationDict(TypedDict):
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    participant_sid: NotRequired[str | None]
    participant_user_sid: NotRequired[str | None]
    participant_identity: NotRequired[str | None]
    participant_messaging_binding: NotRequired[Any | None]
    conversation_sid: NotRequired[str | None]
    conversation_unique_name: NotRequired[str | None]
    conversation_friendly_name: NotRequired[str | None]
    conversation_attributes: NotRequired[str | None]
    conversation_date_created: NotRequired[RFC3339DateTime | None]
    conversation_date_updated: NotRequired[RFC3339DateTime | None]
    conversation_created_by: NotRequired[str | None]
    conversation_state: NotRequired[ParticipantConversationEnumStateOrStr]
    conversation_timers: NotRequired[Any | None]
    links: NotRequired[Any | None]
