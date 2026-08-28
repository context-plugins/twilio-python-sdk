from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1ConversationConversationParticipant(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    participant."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for
    this participant."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    identity: OptionalNullable[str] = UNSET
    """A unique string identifier for the conversation participant as `Conversation User
    <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and only if) the
    participant is using the Conversations SDK to communicate. Limited to 256 characters."""

    attributes: OptionalNullable[str] = UNSET
    """An optional string metadata field you can use to store any data you wish. The string value must contain
    structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned."""

    messaging_binding: OptionalNullable[Any] = UNSET
    """Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of
    type and address fields of the participant."""

    role_sid: OptionalNullable[str] = UNSET
    """The SID of a conversation-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign
    to the participant."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this participant."""

    last_read_message_index: OptionalNullable[int] = UNSET
    """Index of last “read” message in the `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant."""

    last_read_timestamp: OptionalNullable[str] = UNSET
    """Timestamp of last “read” message in the `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant."""


class ConversationsV1ConversationConversationParticipantDict(TypedDict):
    account_sid: NotRequired[str | None]
    conversation_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    attributes: NotRequired[str | None]
    messaging_binding: NotRequired[Any | None]
    role_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    last_read_message_index: NotRequired[int | None]
    last_read_timestamp: NotRequired[str | None]
