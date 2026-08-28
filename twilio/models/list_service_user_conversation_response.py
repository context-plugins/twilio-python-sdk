from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_user_service_user_conversation import (
    ConversationsV1ServiceServiceUserServiceUserConversation,
    ConversationsV1ServiceServiceUserServiceUserConversationDict,
)
from .meta import Meta, MetaDict


class ListServiceUserConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1ServiceServiceUserServiceUserConversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceUserConversationResponseDict(TypedDict):
    conversations: NotRequired[
        list[
            (
                ConversationsV1ServiceServiceUserServiceUserConversation
                | ConversationsV1ServiceServiceUserServiceUserConversationDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
