from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.conference_participant_enum_call_direction import ConferenceParticipantEnumCallDirectionOrStr
from .enums.conference_participant_enum_call_status import ConferenceParticipantEnumCallStatusOrStr
from .enums.conference_participant_enum_call_type import ConferenceParticipantEnumCallTypeOrStr
from .enums.conference_participant_enum_jitter_buffer_size import ConferenceParticipantEnumJitterBufferSizeOrStr
from .enums.conference_participant_enum_processing_state import ConferenceParticipantEnumProcessingStateOrStr
from .enums.conference_participant_enum_region import ConferenceParticipantEnumRegionOrStr


class InsightsV1ConferenceConferenceParticipant(SdkBaseModel):
    participant_sid: OptionalNullable[str] = UNSET
    """SID for this participant."""

    label: OptionalNullable[str] = UNSET
    """The user-specified label of this participant."""

    conference_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Conference."""

    call_sid: OptionalNullable[str] = UNSET
    """Unique SID identifier of the call that generated the Participant resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    call_direction: Optional[ConferenceParticipantEnumCallDirectionOrStr] = UNSET
    from_: OptionalNullable[str] = Field(default=UNSET, alias="from")
    """Caller ID of the calling party."""

    to: OptionalNullable[str] = UNSET
    """Called party."""

    call_status: Optional[ConferenceParticipantEnumCallStatusOrStr] = UNSET
    country_code: OptionalNullable[str] = UNSET
    """ISO alpha-2 country code of the participant based on caller ID or called number."""

    is_moderator: OptionalNullable[bool] = UNSET
    """Boolean. Indicates whether participant had startConferenceOnEnter=true or endConferenceOnExit=true."""

    join_time: OptionalNullable[RFC3339DateTime] = UNSET
    """ISO 8601 timestamp of participant join event."""

    leave_time: OptionalNullable[RFC3339DateTime] = UNSET
    """ISO 8601 timestamp of participant leave event."""

    duration_seconds: OptionalNullable[int] = UNSET
    """Participant durations in seconds."""

    outbound_queue_length: OptionalNullable[int] = UNSET
    """Add Participant API only. Estimated time in queue at call creation."""

    outbound_time_in_queue: OptionalNullable[int] = UNSET
    """Add Participant API only. Actual time in queue in seconds."""

    jitter_buffer_size: Optional[ConferenceParticipantEnumJitterBufferSizeOrStr] = UNSET
    is_coach: OptionalNullable[bool] = UNSET
    """Boolean. Indicated whether participant was a coach."""

    coached_participants: Optional[list[str | None]] = UNSET
    """Call SIDs coached by this participant."""

    participant_region: Optional[ConferenceParticipantEnumRegionOrStr] = UNSET
    conference_region: Optional[ConferenceParticipantEnumRegionOrStr] = UNSET
    call_type: Optional[ConferenceParticipantEnumCallTypeOrStr] = UNSET
    processing_state: Optional[ConferenceParticipantEnumProcessingStateOrStr] = UNSET
    properties: OptionalNullable[Any] = UNSET
    """Participant properties and metadata."""

    events: OptionalNullable[Any] = UNSET
    """Object containing information of actions taken by participants. Contains a dictionary of URL links to nested
    resources of this Conference Participant."""

    metrics: OptionalNullable[Any] = UNSET
    """Object. Contains participant call quality metrics."""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class InsightsV1ConferenceConferenceParticipantDict(TypedDict):
    participant_sid: NotRequired[str | None]
    label: NotRequired[str | None]
    conference_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    call_direction: NotRequired[ConferenceParticipantEnumCallDirectionOrStr]
    from_: NotRequired[str | None]
    to: NotRequired[str | None]
    call_status: NotRequired[ConferenceParticipantEnumCallStatusOrStr]
    country_code: NotRequired[str | None]
    is_moderator: NotRequired[bool | None]
    join_time: NotRequired[RFC3339DateTime | None]
    leave_time: NotRequired[RFC3339DateTime | None]
    duration_seconds: NotRequired[int | None]
    outbound_queue_length: NotRequired[int | None]
    outbound_time_in_queue: NotRequired[int | None]
    jitter_buffer_size: NotRequired[ConferenceParticipantEnumJitterBufferSizeOrStr]
    is_coach: NotRequired[bool | None]
    coached_participants: NotRequired[list[str | None]]
    participant_region: NotRequired[ConferenceParticipantEnumRegionOrStr]
    conference_region: NotRequired[ConferenceParticipantEnumRegionOrStr]
    call_type: NotRequired[ConferenceParticipantEnumCallTypeOrStr]
    processing_state: NotRequired[ConferenceParticipantEnumProcessingStateOrStr]
    properties: NotRequired[Any | None]
    events: NotRequired[Any | None]
    metrics: NotRequired[Any | None]
    url: NotRequired[str | None]
