from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_participant_conversation import (
    ConversationsV1ParticipantConversation,
    ConversationsV1ParticipantConversationDict,
)
from .meta import Meta, MetaDict


class ListParticipantConversationResponse(SdkBaseModel):
    conversations: Optional[list[ConversationsV1ParticipantConversation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListParticipantConversationResponseDict(TypedDict):
    conversations: NotRequired[
        list[ConversationsV1ParticipantConversation | ConversationsV1ParticipantConversationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
