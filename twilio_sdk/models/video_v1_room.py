from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.recording_transcription_enum_status import RecordingTranscriptionEnumStatusOrStr
from .enums.room_enum_room_type import RoomEnumRoomTypeOrStr
from .enums.room_enum_video_codec import RoomEnumVideoCodecOrStr


class VideoV1Room(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that Twilio created to identify the Room resource."""

    status: Optional[RecordingTranscriptionEnumStatusOrStr] = UNSET
    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Room resource."""

    enable_turn: OptionalNullable[bool] = UNSET
    """Deprecated, now always considered to be true."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used as a ``room_sid`` in place of
    the resource's ``sid`` in the URL to address the resource, assuming it does not contain any `reserved characters
    <https://tools.ietf.org/html/rfc3986#section-2.2>`__ that would need to be URL encoded. This value is unique for
    ``in-progress`` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in
    place of the Room SID to interact with the room as long as the room is ``in-progress``."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL Twilio calls using the ``status_callback_method`` to send status information to your application on every
    room event. See `Status Callbacks <https://www.twilio.com/docs/video/api/status-callbacks>`__ for more info."""

    status_callback_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method Twilio uses to call ``status_callback``. Can be ``POST`` or ``GET`` and defaults to ``POST``."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The UTC end time of the room in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format."""

    duration: OptionalNullable[int] = UNSET
    """The duration of the room in seconds."""

    type_: Optional[RoomEnumRoomTypeOrStr] = Field(default=UNSET, alias="type")
    """Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small`` are
    deprecated."""

    max_participants: Optional[int] = UNSET
    """The maximum number of concurrent Participants allowed in the room."""

    max_participant_duration: Optional[int] = UNSET
    """The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400
    seconds (24 hours). The default is 14400 seconds (4 hours)."""

    max_concurrent_published_tracks: OptionalNullable[int] = UNSET
    """The maximum number of published audio, video, and data tracks all participants combined are allowed to publish in
    the room at the same time. Check `Programmable Video Limits
    <https://www.twilio.com/docs/video/programmable-video-limits>`__ for more details. If it is set to 0 it means
    unconstrained."""

    record_participants_on_connect: OptionalNullable[bool] = UNSET
    """Whether to start recording when Participants connect."""

    video_codecs: Optional[list[RoomEnumVideoCodecOrStr | None]] = UNSET
    """An array of the video codecs that are supported when publishing a track in the room. Can be: ``VP8`` and
    ``H264``."""

    media_region: OptionalNullable[str] = UNSET
    """The region for the Room's media server. Can be one of the `available Media Regions
    <https://www.twilio.com/docs/video/ip-addresses#media-servers>`__."""

    audio_only: OptionalNullable[bool] = UNSET
    """When set to true, indicates that the participants in the room will only publish audio. No video tracks will be
    allowed."""

    empty_room_timeout: Optional[int] = UNSET
    """Specifies how long (in minutes) a room will remain active after last participant leaves. Can be configured when
    creating a room via REST API. For Ad-Hoc rooms this value cannot be changed."""

    unused_room_timeout: Optional[int] = UNSET
    """Specifies how long (in minutes) a room will remain active if no one joins. Can be configured when creating a room
    via REST API. For Ad-Hoc rooms this value cannot be changed."""

    large_room: OptionalNullable[bool] = UNSET
    """Indicates if this is a large room."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class VideoV1RoomDict(TypedDict):
    sid: NotRequired[str | None]
    status: NotRequired[RecordingTranscriptionEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    account_sid: NotRequired[str | None]
    enable_turn: NotRequired[bool | None]
    unique_name: NotRequired[str | None]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration: NotRequired[int | None]
    type_: NotRequired[RoomEnumRoomTypeOrStr]
    max_participants: NotRequired[int]
    max_participant_duration: NotRequired[int]
    max_concurrent_published_tracks: NotRequired[int | None]
    record_participants_on_connect: NotRequired[bool | None]
    video_codecs: NotRequired[list[RoomEnumVideoCodecOrStr | None]]
    media_region: NotRequired[str | None]
    audio_only: NotRequired[bool | None]
    empty_room_timeout: NotRequired[int]
    unused_room_timeout: NotRequired[int]
    large_room: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
