from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room_room_participant import VideoV1RoomRoomParticipant, VideoV1RoomRoomParticipantDict


class ListRoomParticipantResponse(SdkBaseModel):
    participants: Optional[list[VideoV1RoomRoomParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomParticipantResponseDict(TypedDict):
    participants: NotRequired[list[VideoV1RoomRoomParticipant | VideoV1RoomRoomParticipantDict]]
    meta: NotRequired[Meta | MetaDict]
