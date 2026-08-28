from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ConversationsV1ServiceServiceConfigurationServiceNotification(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    configuration."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ the
    Configuration applies to."""

    new_message: OptionalNullable[Any] = UNSET
    """The Push Notification configuration for New Messages."""

    added_to_conversation: OptionalNullable[Any] = UNSET
    """The Push Notification configuration for being added to a Conversation."""

    removed_from_conversation: OptionalNullable[Any] = UNSET
    """The Push Notification configuration for being removed from a Conversation."""

    log_enabled: OptionalNullable[bool] = UNSET
    """Weather the notification logging is enabled."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this configuration."""


class ConversationsV1ServiceServiceConfigurationServiceNotificationDict(TypedDict):
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    new_message: NotRequired[Any | None]
    added_to_conversation: NotRequired[Any | None]
    removed_from_conversation: NotRequired[Any | None]
    log_enabled: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
