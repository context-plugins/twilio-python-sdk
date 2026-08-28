from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_conversation import ConversationsV1Conversation, ConversationsV1ConversationDict
from .meta import Meta, MetaDict


class ListConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1Conversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConversationResponseDict(TypedDict):
    conversations: NotRequired[list[ConversationsV1Conversation | ConversationsV1ConversationDict]]
    meta: NotRequired[Meta | MetaDict]
