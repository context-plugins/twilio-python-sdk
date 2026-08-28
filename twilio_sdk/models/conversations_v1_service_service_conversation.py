from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.service_conversation_enum_state import ServiceConversationEnumStateOrStr


class ConversationsV1ServiceServiceConversation(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    conversation."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__
    this conversation belongs to."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ this
    conversation belongs to."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this conversation, limited to 256 characters. Optional."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used to address the resource in
    place of the resource's ``sid`` in the URL."""

    attributes: OptionalNullable[str] = UNSET
    """An optional string metadata field you can use to store any data you wish. The string value must contain
    structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned."""

    state: Optional[ServiceConversationEnumStateOrStr] = UNSET
    """Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or ``closed`` and
    defaults to ``active``"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    timers: OptionalNullable[Any] = UNSET
    """Timer date values representing state update for this conversation."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this conversation."""

    links: OptionalNullable[Any] = UNSET
    """Contains absolute URLs to access the `participants
    <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__, `messages
    <https://www.twilio.com/docs/conversations/api/conversation-message-resource>`__ and `webhooks
    <https://www.twilio.com/docs/conversations/api/conversation-scoped-webhook-resource>`__ of this conversation."""

    bindings: OptionalNullable[Any] = UNSET


class ConversationsV1ServiceServiceConversationDict(TypedDict):
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    attributes: NotRequired[str | None]
    state: NotRequired[ServiceConversationEnumStateOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    timers: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
    bindings: NotRequired[Any | None]
