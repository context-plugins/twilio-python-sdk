from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_video_room_summary import InsightsV1VideoRoomSummary, InsightsV1VideoRoomSummaryDict
from .meta import Meta, MetaDict


class ListVideoRoomSummaryResponse(SdkBaseModel):
    rooms: Optional[list[InsightsV1VideoRoomSummary]] = UNSET
    meta: Optional[Meta] = UNSET


class ListVideoRoomSummaryResponseDict(TypedDict):
    rooms: NotRequired[list[InsightsV1VideoRoomSummary | InsightsV1VideoRoomSummaryDict]]
    meta: NotRequired[Meta | MetaDict]
