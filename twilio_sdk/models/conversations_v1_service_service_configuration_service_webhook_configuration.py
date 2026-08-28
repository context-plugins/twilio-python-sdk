from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr


class ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this service."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__
    this conversation belongs to."""

    pre_webhook_url: OptionalNullable[AnyUrl] = UNSET
    """The absolute url the pre-event webhook request should be sent to."""

    post_webhook_url: OptionalNullable[AnyUrl] = UNSET
    """The absolute url the post-event webhook request should be sent to."""

    filters: Optional[list[str | None]] = UNSET
    """The list of events that your configured webhook targets will receive. Events not configured here will not fire.
    Possible values are ``onParticipantAdd``, ``onParticipantAdded``, ``onDeliveryUpdated``, ``onConversationUpdated``,
    ``onConversationRemove``, ``onParticipantRemove``, ``onConversationUpdate``, ``onMessageAdd``, ``onMessageRemoved``,
    ``onParticipantUpdated``, ``onConversationAdded``, ``onMessageAdded``, ``onConversationAdd``,
    ``onConversationRemoved``, ``onParticipantUpdate``, ``onMessageRemove``, ``onMessageUpdated``,
    ``onParticipantRemoved``, ``onMessageUpdate`` or ``onConversationStateUpdated``."""

    method: Optional[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method to be used when sending a webhook request. One of ``GET`` or ``POST``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this webhook."""


class ConversationsV1ServiceServiceConfigurationServiceWebhookConfigurationDict(TypedDict):
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    pre_webhook_url: NotRequired[AnyUrl | None]
    post_webhook_url: NotRequired[AnyUrl | None]
    filters: NotRequired[list[str | None]]
    method: NotRequired[AmdStatusCallbackMethodOrStr]
    url: NotRequired[AnyUrl | None]
