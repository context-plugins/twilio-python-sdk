from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .conversations_v2_conversation import ConversationsV2Conversation, ConversationsV2ConversationDict
from .meta1 import Meta1, Meta1Dict


class V2ConversationsResponse(SdkBaseModel):
    conversations: list[ConversationsV2Conversation]
    meta: Meta1


class V2ConversationsResponseDict(TypedDict):
    conversations: list[ConversationsV2Conversation | ConversationsV2ConversationDict]
    meta: Meta1 | Meta1Dict
