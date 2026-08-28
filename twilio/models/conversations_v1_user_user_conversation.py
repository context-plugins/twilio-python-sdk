from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.user_conversation_enum_notification_level import UserConversationEnumNotificationLevelOrStr
from .enums.user_conversation_enum_state import UserConversationEnumStateOrStr


class ConversationsV1UserUserConversation(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    conversation."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__
    this conversation belongs to."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for
    this User Conversation."""

    unread_messages_count: OptionalNullable[int] = UNSET
    """The number of unread Messages in the Conversation for the Participant."""

    last_read_message_index: OptionalNullable[int] = UNSET
    """The index of the last Message in the Conversation that the Participant has read."""

    participant_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `participant
    <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ the user conversation belongs
    to."""

    user_sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the `User resource
    <https://www.twilio.com/docs/conversations/api/user-resource>`__."""

    friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this conversation, limited to 256 characters. Optional."""

    conversation_state: Optional[UserConversationEnumStateOrStr] = UNSET
    """The current state of this User Conversation. One of ``inactive``, ``active`` or ``closed``."""

    timers: OptionalNullable[Any] = UNSET
    """Timer date values representing state update for this conversation."""

    attributes: OptionalNullable[str] = UNSET
    """An optional string metadata field you can use to store any data you wish. The string value must contain
    structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this conversation was created, given in ISO 8601 format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this conversation was last updated, given in ISO 8601 format."""

    created_by: OptionalNullable[str] = UNSET
    """Identity of the creator of this Conversation."""

    notification_level: Optional[UserConversationEnumNotificationLevelOrStr] = UNSET
    """The Notification Level of this User Conversation. One of ``default`` or ``muted``."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the Conversation resource. It can be used to address the
    resource in place of the resource's ``conversation_sid`` in the URL."""

    url: OptionalNullable[str] = UNSET
    links: OptionalNullable[Any] = UNSET
    """Contains absolute URLs to access the `participant
    <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ and `conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ of this conversation."""


class ConversationsV1UserUserConversationDict(TypedDict):
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    conversation_sid: NotRequired[str | None]
    unread_messages_count: NotRequired[int | None]
    last_read_message_index: NotRequired[int | None]
    participant_sid: NotRequired[str | None]
    user_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    conversation_state: NotRequired[UserConversationEnumStateOrStr]
    timers: NotRequired[Any | None]
    attributes: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    created_by: NotRequired[str | None]
    notification_level: NotRequired[UserConversationEnumNotificationLevelOrStr]
    unique_name: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
