from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.video_room_summary_enum_codec import VideoRoomSummaryEnumCodecOrStr
from .enums.video_room_summary_enum_created_method import VideoRoomSummaryEnumCreatedMethodOrStr
from .enums.video_room_summary_enum_edge_location import VideoRoomSummaryEnumEdgeLocationOrStr
from .enums.video_room_summary_enum_end_reason import VideoRoomSummaryEnumEndReasonOrStr
from .enums.video_room_summary_enum_processing_state import VideoRoomSummaryEnumProcessingStateOrStr
from .enums.video_room_summary_enum_room_status import VideoRoomSummaryEnumRoomStatusOrStr
from .enums.video_room_summary_enum_room_type import VideoRoomSummaryEnumRoomTypeOrStr
from .enums.video_room_summary_enum_twilio_realm import VideoRoomSummaryEnumTwilioRealmOrStr


class InsightsV1VideoRoomSummary(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """Account SID associated with this room."""

    room_sid: OptionalNullable[str] = UNSET
    """Unique identifier for the room."""

    room_name: OptionalNullable[str] = UNSET
    """Room friendly name."""

    create_time: OptionalNullable[RFC3339DateTime] = UNSET
    """Creation time of the room."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """End time for the room."""

    room_type: Optional[VideoRoomSummaryEnumRoomTypeOrStr] = UNSET
    room_status: Optional[VideoRoomSummaryEnumRoomStatusOrStr] = UNSET
    status_callback: OptionalNullable[AnyUrl] = UNSET
    """Webhook provided for status callbacks."""

    status_callback_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """HTTP method provided for status callback URL."""

    created_method: Optional[VideoRoomSummaryEnumCreatedMethodOrStr] = UNSET
    end_reason: Optional[VideoRoomSummaryEnumEndReasonOrStr] = UNSET
    max_participants: OptionalNullable[int] = UNSET
    """Max number of total participants allowed by the application settings."""

    unique_participants: OptionalNullable[int] = UNSET
    """Number of participants. May include duplicate identities for participants who left and rejoined."""

    unique_participant_identities: OptionalNullable[int] = UNSET
    """Unique number of participant identities."""

    concurrent_participants: OptionalNullable[int] = UNSET
    """Actual number of concurrent participants."""

    max_concurrent_participants: OptionalNullable[int] = UNSET
    """Maximum number of participants allowed in the room at the same time allowed by the application settings."""

    codecs: Optional[list[VideoRoomSummaryEnumCodecOrStr | None]] = UNSET
    """Codecs used by participants in the room. Can be ``VP8``, ``H264``, or ``VP9``."""

    media_region: Optional[VideoRoomSummaryEnumTwilioRealmOrStr] = UNSET
    duration_sec: OptionalNullable[int] = UNSET
    """Total room duration from create time to end time."""

    total_participant_duration_sec: OptionalNullable[int] = UNSET
    """Combined amount of participant time in the room."""

    total_recording_duration_sec: OptionalNullable[int] = UNSET
    """Combined amount of recorded seconds for participants in the room."""

    processing_state: Optional[VideoRoomSummaryEnumProcessingStateOrStr] = UNSET
    recording_enabled: OptionalNullable[bool] = UNSET
    """Boolean indicating if recording is enabled for the room."""

    edge_location: Optional[VideoRoomSummaryEnumEdgeLocationOrStr] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET
    """URL for the room resource."""

    links: OptionalNullable[Any] = UNSET
    """Room subresources."""


class InsightsV1VideoRoomSummaryDict(TypedDict):
    account_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    room_name: NotRequired[str | None]
    create_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    room_type: NotRequired[VideoRoomSummaryEnumRoomTypeOrStr]
    room_status: NotRequired[VideoRoomSummaryEnumRoomStatusOrStr]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    created_method: NotRequired[VideoRoomSummaryEnumCreatedMethodOrStr]
    end_reason: NotRequired[VideoRoomSummaryEnumEndReasonOrStr]
    max_participants: NotRequired[int | None]
    unique_participants: NotRequired[int | None]
    unique_participant_identities: NotRequired[int | None]
    concurrent_participants: NotRequired[int | None]
    max_concurrent_participants: NotRequired[int | None]
    codecs: NotRequired[list[VideoRoomSummaryEnumCodecOrStr | None]]
    media_region: NotRequired[VideoRoomSummaryEnumTwilioRealmOrStr]
    duration_sec: NotRequired[int | None]
    total_participant_duration_sec: NotRequired[int | None]
    total_recording_duration_sec: NotRequired[int | None]
    processing_state: NotRequired[VideoRoomSummaryEnumProcessingStateOrStr]
    recording_enabled: NotRequired[bool | None]
    edge_location: NotRequired[VideoRoomSummaryEnumEdgeLocationOrStr]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
