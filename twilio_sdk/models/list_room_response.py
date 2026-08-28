from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room import VideoV1Room, VideoV1RoomDict


class ListRoomResponse(SdkBaseModel):
    rooms: Optional[list[VideoV1Room]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomResponseDict(TypedDict):
    rooms: NotRequired[list[VideoV1Room | VideoV1RoomDict]]
    meta: NotRequired[Meta | MetaDict]
