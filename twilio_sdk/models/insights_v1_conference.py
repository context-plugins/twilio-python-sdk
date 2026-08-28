from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.conference_enum_conference_end_reason import ConferenceEnumConferenceEndReasonOrStr
from .enums.conference_enum_conference_status import ConferenceEnumConferenceStatusOrStr
from .enums.conference_enum_processing_state import ConferenceEnumProcessingStateOrStr
from .enums.conference_enum_region import ConferenceEnumRegionOrStr
from .enums.conference_enum_tag import ConferenceEnumTagOrStr


class InsightsV1Conference(SdkBaseModel):
    conference_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Conference."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    friendly_name: OptionalNullable[str] = UNSET
    """Custom label for the conference resource, up to 64 characters."""

    create_time: OptionalNullable[RFC3339DateTime] = UNSET
    """Conference creation date and time in ISO 8601 format."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in ISO 8601 format when the conference started. Conferences do not start until at least two
    participants join, at least one of whom has startConferenceOnEnter=true."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """Conference end date and time in ISO 8601 format."""

    duration_seconds: OptionalNullable[int] = UNSET
    """Conference duration in seconds."""

    connect_duration_seconds: OptionalNullable[int] = UNSET
    """Duration of the between conference start event and conference end event in seconds."""

    status: Optional[ConferenceEnumConferenceStatusOrStr] = UNSET
    max_participants: OptionalNullable[int] = UNSET
    """Maximum number of concurrent participants as specified by the configuration."""

    max_concurrent_participants: OptionalNullable[int] = UNSET
    """Actual maximum number of concurrent participants in the conference."""

    unique_participants: OptionalNullable[int] = UNSET
    """Unique conference participants based on caller ID."""

    end_reason: Optional[ConferenceEnumConferenceEndReasonOrStr] = UNSET
    ended_by: OptionalNullable[str] = UNSET
    """Call SID of the participant whose actions ended the conference."""

    mixer_region: Optional[ConferenceEnumRegionOrStr] = UNSET
    mixer_region_requested: Optional[ConferenceEnumRegionOrStr] = UNSET
    recording_enabled: OptionalNullable[bool] = UNSET
    """Boolean. Indicates whether recording was enabled at the conference mixer."""

    detected_issues: OptionalNullable[Any] = UNSET
    """Potential issues detected by Twilio during the conference."""

    tags: Optional[list[ConferenceEnumTagOrStr | None]] = UNSET
    """Tags for detected conference conditions and participant behaviors which may be of interest."""

    tag_info: OptionalNullable[Any] = UNSET
    """Object. Contains details about conference tags including severity."""

    processing_state: Optional[ConferenceEnumProcessingStateOrStr] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""

    links: OptionalNullable[Any] = UNSET
    """Contains a dictionary of URL links to nested resources of this Conference."""


class InsightsV1ConferenceDict(TypedDict):
    conference_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    create_time: NotRequired[RFC3339DateTime | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration_seconds: NotRequired[int | None]
    connect_duration_seconds: NotRequired[int | None]
    status: NotRequired[ConferenceEnumConferenceStatusOrStr]
    max_participants: NotRequired[int | None]
    max_concurrent_participants: NotRequired[int | None]
    unique_participants: NotRequired[int | None]
    end_reason: NotRequired[ConferenceEnumConferenceEndReasonOrStr]
    ended_by: NotRequired[str | None]
    mixer_region: NotRequired[ConferenceEnumRegionOrStr]
    mixer_region_requested: NotRequired[ConferenceEnumRegionOrStr]
    recording_enabled: NotRequired[bool | None]
    detected_issues: NotRequired[Any | None]
    tags: NotRequired[list[ConferenceEnumTagOrStr | None]]
    tag_info: NotRequired[Any | None]
    processing_state: NotRequired[ConferenceEnumProcessingStateOrStr]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
