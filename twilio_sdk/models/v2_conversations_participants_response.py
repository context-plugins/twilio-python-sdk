from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .conversations_v2_participant import ConversationsV2Participant, ConversationsV2ParticipantDict
from .meta2 import Meta2, Meta2Dict


class V2ConversationsParticipantsResponse(SdkBaseModel):
    participants: list[ConversationsV2Participant]
    meta: Meta2


class V2ConversationsParticipantsResponseDict(TypedDict):
    participants: list[ConversationsV2Participant | ConversationsV2ParticipantDict]
    meta: Meta2 | Meta2Dict
