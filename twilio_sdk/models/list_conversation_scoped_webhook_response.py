from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_conversation_conversation_scoped_webhook import (
    ConversationsV1ConversationConversationScopedWebhook,
    ConversationsV1ConversationConversationScopedWebhookDict,
)
from .meta import Meta, MetaDict


class ListConversationScopedWebhookResponse(SdkBaseModel):
    webhooks: Optional[list[ConversationsV1ConversationConversationScopedWebhook]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConversationScopedWebhookResponseDict(TypedDict):
    webhooks: NotRequired[
        list[
            (
                ConversationsV1ConversationConversationScopedWebhook
                | ConversationsV1ConversationConversationScopedWebhookDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
