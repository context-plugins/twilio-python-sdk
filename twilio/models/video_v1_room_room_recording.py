from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_recording_enum_codec import RoomRecordingEnumCodecOrStr
from .enums.room_recording_enum_format import RoomRecordingEnumFormatOrStr
from .enums.room_recording_enum_status import RoomRecordingEnumStatusOrStr
from .enums.room_recording_enum_type import RoomRecordingEnumTypeOrStr


class VideoV1RoomRoomRecording(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the RoomRecording
    resource."""

    status: Optional[RoomRecordingEnumStatusOrStr] = UNSET
    """The status of the recording. Can be: ``processing``, ``completed``, or ``deleted``. ``processing`` indicates the
    Recording is still being captured. ``completed`` indicates the Recording has been captured and is now available for
    download. ``deleted`` means the recording media has been deleted from the system, but its metadata is still
    available for historical purposes."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the RoomRecording resource."""

    source_sid: OptionalNullable[str] = UNSET
    """The SID of the recording source. For a Room Recording, this value is a ``track_sid``."""

    size: OptionalNullable[int] = UNSET
    """The size of the recorded track in bytes."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""

    type_: Optional[RoomRecordingEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The recording's media type. Can be: ``audio`` or ``video``."""

    duration: OptionalNullable[int] = UNSET
    """The duration of the recording rounded to the nearest second. Sub-second duration tracks have a ``duration`` of 1
    second"""

    container_format: Optional[RoomRecordingEnumFormatOrStr] = UNSET
    codec: Optional[RoomRecordingEnumCodecOrStr] = UNSET
    """The codec used for the recording. Can be: ``VP8`` or ``H264``."""

    grouping_sids: OptionalNullable[Any] = UNSET
    """A list of SIDs related to the Recording. Includes the ``room_sid`` and ``participant_sid``."""

    track_name: OptionalNullable[str] = UNSET
    """The name that was given to the source track of the recording. If no name is given, the ``source_sid`` is used."""

    offset: OptionalNullable[int] = UNSET
    """The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment
    when the source room of this track started. This information provides a synchronization mechanism for recordings
    belonging to the same room."""

    media_external_location: OptionalNullable[str] = UNSET
    """The URL of the media file associated with the recording when stored externally. See `External S3 Recordings
    </docs/video/api/external-s3-recordings>`__ for more details."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the Room resource the recording is associated with."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class VideoV1RoomRoomRecordingDict(TypedDict):
    account_sid: NotRequired[str | None]
    status: NotRequired[RoomRecordingEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    source_sid: NotRequired[str | None]
    size: NotRequired[int | None]
    url: NotRequired[str | None]
    type_: NotRequired[RoomRecordingEnumTypeOrStr]
    duration: NotRequired[int | None]
    container_format: NotRequired[RoomRecordingEnumFormatOrStr]
    codec: NotRequired[RoomRecordingEnumCodecOrStr]
    grouping_sids: NotRequired[Any | None]
    track_name: NotRequired[str | None]
    offset: NotRequired[int | None]
    media_external_location: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    links: NotRequired[Any | None]
