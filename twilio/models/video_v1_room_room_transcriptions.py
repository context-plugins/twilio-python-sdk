from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_transcriptions_enum_status import RoomTranscriptionsEnumStatusOrStr


class VideoV1RoomRoomTranscriptions(SdkBaseModel):
    ttid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the transcriptions resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Room resource."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the transcriptions's room."""

    source_sid: OptionalNullable[str] = UNSET
    """The SID of the transcriptions's associated call."""

    status: Optional[RoomTranscriptionsEnumStatusOrStr] = UNSET
    """The status of the transcriptions resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time of transcriptions connected to the room in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__
    format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time when the transcriptions disconnected from the room in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format."""

    duration: OptionalNullable[int] = UNSET
    """The duration in seconds that the transcriptions were ``connected``. Populated only after the transcriptions is
    ``stopped``."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""

    configuration: OptionalNullable[Any] = UNSET
    """An JSON object that describes the video layout of the composition in terms of regions. See `Specifying Video
    Layouts <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info."""


class VideoV1RoomRoomTranscriptionsDict(TypedDict):
    ttid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    source_sid: NotRequired[str | None]
    status: NotRequired[RoomTranscriptionsEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration: NotRequired[int | None]
    url: NotRequired[str | None]
    configuration: NotRequired[Any | None]
