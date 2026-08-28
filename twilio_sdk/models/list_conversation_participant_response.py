from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_conversation_conversation_participant import (
    ConversationsV1ConversationConversationParticipant,
    ConversationsV1ConversationConversationParticipantDict,
)
from .meta import Meta, MetaDict


class ListConversationParticipantResponse(SdkBaseModel):
    participants: Optional[list[ConversationsV1ConversationConversationParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConversationParticipantResponseDict(TypedDict):
    participants: NotRequired[
        list[
            ConversationsV1ConversationConversationParticipant | ConversationsV1ConversationConversationParticipantDict
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
