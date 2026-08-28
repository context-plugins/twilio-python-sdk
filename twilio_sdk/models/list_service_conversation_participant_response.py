from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_conversation_service_conversation_participant import (
    ConversationsV1ServiceServiceConversationServiceConversationParticipant,
    ConversationsV1ServiceServiceConversationServiceConversationParticipantDict,
)
from .meta import Meta, MetaDict


class ListServiceConversationParticipantResponse(SdkBaseModel):
    participants: Optional[list[ConversationsV1ServiceServiceConversationServiceConversationParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceConversationParticipantResponseDict(TypedDict):
    participants: NotRequired[
        list[
            (
                ConversationsV1ServiceServiceConversationServiceConversationParticipant
                | ConversationsV1ServiceServiceConversationServiceConversationParticipantDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
