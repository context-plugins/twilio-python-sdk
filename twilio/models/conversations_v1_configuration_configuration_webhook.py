from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.configuration_webhook_enum_target import ConfigurationWebhookEnumTargetOrStr


class ConversationsV1ConfigurationConfigurationWebhook(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    conversation."""

    method: Optional[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method to be used when sending a webhook request."""

    filters: Optional[list[str | None]] = UNSET
    """The list of webhook event triggers that are enabled for this Service: ``onMessageAdded``, ``onMessageUpdated``,
    ``onMessageRemoved``, ``onMessageAdd``, ``onMessageUpdate``, ``onMessageRemove``, ``onConversationUpdated``,
    ``onConversationRemoved``, ``onConversationAdd``, ``onConversationAdded``, ``onConversationRemove``,
    ``onConversationUpdate``, ``onConversationStateUpdated``, ``onParticipantAdded``, ``onParticipantUpdated``,
    ``onParticipantRemoved``, ``onParticipantAdd``, ``onParticipantRemove``, ``onParticipantUpdate``,
    ``onDeliveryUpdated``, ``onUserAdded``, ``onUserUpdate``, ``onUserUpdated``"""

    pre_webhook_url: OptionalNullable[str] = UNSET
    """The absolute url the pre-event webhook request should be sent to."""

    post_webhook_url: OptionalNullable[str] = UNSET
    """The absolute url the post-event webhook request should be sent to."""

    target: Optional[ConfigurationWebhookEnumTargetOrStr] = UNSET
    """The routing target of the webhook. Can be ordinary or route internally to Flex"""

    url: OptionalNullable[str] = UNSET
    """An absolute API resource API resource URL for this webhook."""


class ConversationsV1ConfigurationConfigurationWebhookDict(TypedDict):
    account_sid: NotRequired[str | None]
    method: NotRequired[AmdStatusCallbackMethodOrStr]
    filters: NotRequired[list[str | None]]
    pre_webhook_url: NotRequired[str | None]
    post_webhook_url: NotRequired[str | None]
    target: NotRequired[ConfigurationWebhookEnumTargetOrStr]
    url: NotRequired[str | None]
