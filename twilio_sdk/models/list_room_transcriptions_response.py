from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room_room_transcriptions import VideoV1RoomRoomTranscriptions, VideoV1RoomRoomTranscriptionsDict


class ListRoomTranscriptionsResponse(SdkBaseModel):
    transcriptions: Optional[list[VideoV1RoomRoomTranscriptions]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomTranscriptionsResponseDict(TypedDict):
    transcriptions: NotRequired[list[VideoV1RoomRoomTranscriptions | VideoV1RoomRoomTranscriptionsDict]]
    meta: NotRequired[Meta | MetaDict]
