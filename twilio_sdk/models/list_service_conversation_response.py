from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_conversation import (
    ConversationsV1ServiceServiceConversation,
    ConversationsV1ServiceServiceConversationDict,
)
from .meta import Meta, MetaDict


class ListServiceConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1ServiceServiceConversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceConversationResponseDict(TypedDict):
    conversations: NotRequired[
        list[ConversationsV1ServiceServiceConversation | ConversationsV1ServiceServiceConversationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
