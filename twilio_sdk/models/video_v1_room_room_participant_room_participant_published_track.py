from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_participant_published_track_enum_kind import RoomParticipantPublishedTrackEnumKindOrStr


class VideoV1RoomRoomParticipantRoomParticipantPublishedTrack(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the RoomParticipantPublishedTrack resource."""

    participant_sid: OptionalNullable[str] = UNSET
    """The SID of the Participant resource with the published track."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the Room resource where the track is published."""

    name: OptionalNullable[str] = UNSET
    """The track name. Must be no more than 128 characters, and be unique among the participant's published tracks."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    enabled: OptionalNullable[bool] = UNSET
    """Whether the track is enabled."""

    kind: Optional[RoomParticipantPublishedTrackEnumKindOrStr] = UNSET
    """The track type. Can be: ``audio``, ``video`` or ``data``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class VideoV1RoomRoomParticipantRoomParticipantPublishedTrackDict(TypedDict):
    sid: NotRequired[str | None]
    participant_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    enabled: NotRequired[bool | None]
    kind: NotRequired[RoomParticipantPublishedTrackEnumKindOrStr]
    url: NotRequired[AnyUrl | None]
