from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ConversationsV1Configuration(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this configuration."""

    default_chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the default `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__
    used when creating a conversation."""

    default_messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the default `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ used
    when creating a conversation."""

    default_inactive_timer: OptionalNullable[str] = UNSET
    """Default ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value for this timer
    is 1 minute."""

    default_closed_timer: OptionalNullable[str] = UNSET
    """Default ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for this timer is
    10 minutes."""

    url: OptionalNullable[str] = UNSET
    """An absolute API resource URL for this global configuration."""

    links: OptionalNullable[Any] = UNSET
    """Contains absolute API resource URLs to access the webhook and default service configurations."""


class ConversationsV1ConfigurationDict(TypedDict):
    account_sid: NotRequired[str | None]
    default_chat_service_sid: NotRequired[str | None]
    default_messaging_service_sid: NotRequired[str | None]
    default_inactive_timer: NotRequired[str | None]
    default_closed_timer: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
