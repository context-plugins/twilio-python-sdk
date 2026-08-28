from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_room_room_participant_room_participant_subscribed_track import (
    VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack,
    VideoV1RoomRoomParticipantRoomParticipantSubscribedTrackDict,
)


class ListRoomParticipantSubscribedTrackResponse(SdkBaseModel):
    subscribed_tracks: Optional[list[VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoomParticipantSubscribedTrackResponseDict(TypedDict):
    subscribed_tracks: NotRequired[
        list[
            (
                VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack
                | VideoV1RoomRoomParticipantRoomParticipantSubscribedTrackDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
