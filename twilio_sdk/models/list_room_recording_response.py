from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room_room_recording import VideoV1RoomRoomRecording, VideoV1RoomRoomRecordingDict


class ListRoomRecordingResponse(SdkBaseModel):
    recordings: Optional[list[VideoV1RoomRoomRecording]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomRecordingResponseDict(TypedDict):
    recordings: NotRequired[list[VideoV1RoomRoomRecording | VideoV1RoomRoomRecordingDict]]
    meta: NotRequired[Meta | MetaDict]
