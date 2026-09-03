from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .conversations_v2_communication import ConversationsV2Communication, ConversationsV2CommunicationDict
from .meta2 import Meta2, Meta2Dict


class V2ConversationsCommunicationsResponse(SdkBaseModel):
    communications: list[ConversationsV2Communication]
    meta: Meta2


class V2ConversationsCommunicationsResponseDict(TypedDict):
    communications: list[ConversationsV2Communication | ConversationsV2CommunicationDict]
    meta: Meta2 | Meta2Dict
