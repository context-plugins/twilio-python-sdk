from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_conversation_service_conversation_message import (
    ConversationsV1ServiceServiceConversationServiceConversationMessage,
    ConversationsV1ServiceServiceConversationServiceConversationMessageDict,
)
from .meta import Meta, MetaDict


class ListServiceConversationMessageResponse(SdkBaseModel):
    messages: Optional[list[ConversationsV1ServiceServiceConversationServiceConversationMessage]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceConversationMessageResponseDict(TypedDict):
    messages: NotRequired[
        list[
            (
                ConversationsV1ServiceServiceConversationServiceConversationMessage
                | ConversationsV1ServiceServiceConversationServiceConversationMessageDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
