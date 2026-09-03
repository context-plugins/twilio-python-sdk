from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_conversation_conversation_message import (
    ConversationsV1ConversationConversationMessage,
    ConversationsV1ConversationConversationMessageDict,
)
from .meta import Meta, MetaDict


class ListConversationMessageResponse(SdkBaseModel):
    messages: Optional[list[ConversationsV1ConversationConversationMessage]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConversationMessageResponseDict(TypedDict):
    messages: NotRequired[
        list[ConversationsV1ConversationConversationMessage | ConversationsV1ConversationConversationMessageDict]
    ]
    meta: NotRequired[Meta | MetaDict]
