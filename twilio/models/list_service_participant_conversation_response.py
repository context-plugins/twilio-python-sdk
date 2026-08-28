from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_participant_conversation import (
    ConversationsV1ServiceServiceParticipantConversation,
    ConversationsV1ServiceServiceParticipantConversationDict,
)
from .meta import Meta, MetaDict


class ListServiceParticipantConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1ServiceServiceParticipantConversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceParticipantConversationResponseDict(TypedDict):
    conversations: NotRequired[
        list[
            (
                ConversationsV1ServiceServiceParticipantConversation
                | ConversationsV1ServiceServiceParticipantConversationDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
