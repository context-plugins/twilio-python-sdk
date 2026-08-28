from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_video_room_summary_video_participant_summary import (
    InsightsV1VideoRoomSummaryVideoParticipantSummary,
    InsightsV1VideoRoomSummaryVideoParticipantSummaryDict,
)
from .meta import Meta, MetaDict


class ListVideoParticipantSummaryResponse(SdkBaseModel):
    participants: Optional[list[InsightsV1VideoRoomSummaryVideoParticipantSummary]] = UNSET
    meta: Optional[Meta] = UNSET


class ListVideoParticipantSummaryResponseDict(TypedDict):
    participants: NotRequired[
        list[InsightsV1VideoRoomSummaryVideoParticipantSummary | InsightsV1VideoRoomSummaryVideoParticipantSummaryDict]
    ]
    meta: NotRequired[Meta | MetaDict]
