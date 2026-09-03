from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_conversation_service_conversation_scoped_webhook import (
    ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook,
    ConversationsV1ServiceServiceConversationServiceConversationScopedWebhookDict,
)
from .meta import Meta, MetaDict


class ListServiceConversationScopedWebhookResponse(SdkBaseModel):
    webhooks: Optional[list[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceConversationScopedWebhookResponseDict(TypedDict):
    webhooks: NotRequired[
        list[
            (
                ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook
                | ConversationsV1ServiceServiceConversationServiceConversationScopedWebhookDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
