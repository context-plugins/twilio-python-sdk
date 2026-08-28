from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_user_user_conversation import (
    ConversationsV1UserUserConversation,
    ConversationsV1UserUserConversationDict,
)
from .meta import Meta, MetaDict


class ListUserConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1UserUserConversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListUserConversationResponseDict(TypedDict):
    conversations: NotRequired[list[ConversationsV1UserUserConversation | ConversationsV1UserUserConversationDict]]
    meta: NotRequired[Meta | MetaDict]
