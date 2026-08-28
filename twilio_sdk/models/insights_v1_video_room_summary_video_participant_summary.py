from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.video_participant_summary_enum_codec import VideoParticipantSummaryEnumCodecOrStr
from .enums.video_participant_summary_enum_edge_location import VideoParticipantSummaryEnumEdgeLocationOrStr
from .enums.video_participant_summary_enum_room_status import VideoParticipantSummaryEnumRoomStatusOrStr
from .enums.video_participant_summary_enum_twilio_realm import VideoParticipantSummaryEnumTwilioRealmOrStr


class InsightsV1VideoRoomSummaryVideoParticipantSummary(SdkBaseModel):
    participant_sid: OptionalNullable[str] = UNSET
    """Unique identifier for the participant."""

    participant_identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the participant within a Room."""

    join_time: OptionalNullable[RFC3339DateTime] = UNSET
    """When the participant joined the room."""

    leave_time: OptionalNullable[RFC3339DateTime] = UNSET
    """When the participant left the room."""

    duration_sec: OptionalNullable[int] = UNSET
    """Amount of time in seconds the participant was in the room."""

    account_sid: OptionalNullable[str] = UNSET
    """Account SID associated with the room."""

    room_sid: OptionalNullable[str] = UNSET
    """Unique identifier for the room."""

    status: Optional[VideoParticipantSummaryEnumRoomStatusOrStr] = UNSET
    codecs: Optional[list[VideoParticipantSummaryEnumCodecOrStr | None]] = UNSET
    """Codecs detected from the participant. Can be ``VP8``, ``H264``, or ``VP9``."""

    end_reason: OptionalNullable[str] = UNSET
    """Reason the participant left the room. See `the list of possible values here
    <https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#end_reason>`__."""

    error_code: OptionalNullable[int] = UNSET
    """Errors encountered by the participant."""

    error_code_url: OptionalNullable[str] = UNSET
    """Twilio error code dictionary link."""

    media_region: Optional[VideoParticipantSummaryEnumTwilioRealmOrStr] = UNSET
    properties: OptionalNullable[Any] = UNSET
    """Object containing information about the participant's data from the room. See `below
    <https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#properties>`__ for more information."""

    edge_location: Optional[VideoParticipantSummaryEnumEdgeLocationOrStr] = UNSET
    publisher_info: OptionalNullable[Any] = UNSET
    """Object containing information about the SDK name and version. See `below
    <https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#publisher_info>`__ for more
    information."""

    url: OptionalNullable[AnyUrl] = UNSET
    """URL of the participant resource."""


class InsightsV1VideoRoomSummaryVideoParticipantSummaryDict(TypedDict):
    participant_sid: NotRequired[str | None]
    participant_identity: NotRequired[str | None]
    join_time: NotRequired[RFC3339DateTime | None]
    leave_time: NotRequired[RFC3339DateTime | None]
    duration_sec: NotRequired[int | None]
    account_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    status: NotRequired[VideoParticipantSummaryEnumRoomStatusOrStr]
    codecs: NotRequired[list[VideoParticipantSummaryEnumCodecOrStr | None]]
    end_reason: NotRequired[str | None]
    error_code: NotRequired[int | None]
    error_code_url: NotRequired[str | None]
    media_region: NotRequired[VideoParticipantSummaryEnumTwilioRealmOrStr]
    properties: NotRequired[Any | None]
    edge_location: NotRequired[VideoParticipantSummaryEnumEdgeLocationOrStr]
    publisher_info: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
