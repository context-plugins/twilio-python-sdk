from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    conversation."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ the
    Participant resource is associated with."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for
    this webhook."""

    target: OptionalNullable[str] = UNSET
    """The target of this webhook: ``webhook``, ``studio``, ``trigger``"""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this webhook."""

    configuration: OptionalNullable[Any] = UNSET
    """The configuration of this webhook. Is defined based on target."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""


class ConversationsV1ServiceServiceConversationServiceConversationScopedWebhookDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    conversation_sid: NotRequired[str | None]
    target: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    configuration: NotRequired[Any | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
