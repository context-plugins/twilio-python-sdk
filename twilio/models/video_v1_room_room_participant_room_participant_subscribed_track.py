from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_participant_subscribed_track_enum_kind import RoomParticipantSubscribedTrackEnumKindOrStr


class VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the RoomParticipantSubscribedTrack resource."""

    participant_sid: OptionalNullable[str] = UNSET
    """The SID of the participant that subscribes to the track."""

    publisher_sid: OptionalNullable[str] = UNSET
    """The SID of the participant that publishes the track."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the room where the track is published."""

    name: OptionalNullable[str] = UNSET
    """The track name. Must have no more than 128 characters and be unique among the participant's published tracks."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    enabled: OptionalNullable[bool] = UNSET
    """Whether the track is enabled."""

    kind: Optional[RoomParticipantSubscribedTrackEnumKindOrStr] = UNSET
    """The track type. Can be: ``audio``, ``video`` or ``data``."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""


class VideoV1RoomRoomParticipantRoomParticipantSubscribedTrackDict(TypedDict):
    sid: NotRequired[str | None]
    participant_sid: NotRequired[str | None]
    publisher_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    enabled: NotRequired[bool | None]
    kind: NotRequired[RoomParticipantSubscribedTrackEnumKindOrStr]
    url: NotRequired[str | None]
