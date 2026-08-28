from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room_room_participant_room_participant_published_track import (
    VideoV1RoomRoomParticipantRoomParticipantPublishedTrack,
    VideoV1RoomRoomParticipantRoomParticipantPublishedTrackDict,
)


class ListRoomParticipantPublishedTrackResponse(SdkBaseModel):
    published_tracks: Optional[list[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomParticipantPublishedTrackResponseDict(TypedDict):
    published_tracks: NotRequired[
        list[
            (
                VideoV1RoomRoomParticipantRoomParticipantPublishedTrack
                | VideoV1RoomRoomParticipantRoomParticipantPublishedTrackDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
