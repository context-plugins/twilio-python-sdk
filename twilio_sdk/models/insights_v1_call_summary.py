from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.summary_enum_answered_by import SummaryEnumAnsweredByOrStr
from .enums.summary_enum_call_state import SummaryEnumCallStateOrStr
from .enums.summary_enum_call_type import SummaryEnumCallTypeOrStr
from .enums.summary_enum_processing_state import SummaryEnumProcessingStateOrStr


class InsightsV1CallSummary(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    call_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Call."""

    call_type: Optional[SummaryEnumCallTypeOrStr] = UNSET
    call_state: Optional[SummaryEnumCallStateOrStr] = UNSET
    answered_by: Optional[SummaryEnumAnsweredByOrStr] = UNSET
    processing_state: Optional[SummaryEnumProcessingStateOrStr] = UNSET
    created_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time at which the Call was created, given in ISO 8601 format. Can be different from ``start_time`` in the
    event of queueing due to CPS"""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time at which the Call was started, given in ISO 8601 format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time at which the Call was ended, given in ISO 8601 format."""

    duration: OptionalNullable[int] = UNSET
    """Duration between when the call was initiated and the call was ended"""

    connect_duration: OptionalNullable[int] = UNSET
    """Duration between when the call was answered and when it ended"""

    from_: OptionalNullable[Any] = Field(default=UNSET, alias="from")
    """``object`` The calling party. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#tofrom-object>`__ for the object
    properties."""

    to: OptionalNullable[Any] = UNSET
    """``object`` The called party. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#tofrom-object>`__ for the object
    properties."""

    carrier_edge: OptionalNullable[Any] = UNSET
    """``object`` Contains metrics and properties for the Twilio media gateway of a PSTN call. See `Details: Call
    Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    client_edge: OptionalNullable[Any] = UNSET
    """``object`` Contains metrics and properties for the Twilio media gateway of a Client call. See `Details: Call
    Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    sdk_edge: OptionalNullable[Any] = UNSET
    """``object`` Contains metrics and properties for the SDK sensor library for Client calls. See `Details: Call
    Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    sip_edge: OptionalNullable[Any] = UNSET
    """``object`` Contains metrics and properties for the Twilio media gateway of a SIP Interface or Trunking call. See
    `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    tags: Optional[list[str | None]] = UNSET
    """Tags applied to calls by Voice Insights analysis indicating a condition that could result in subjective
    degradation of the call quality."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""

    attributes: OptionalNullable[Any] = UNSET
    """``object`` Attributes capturing call-flow-specific details. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#attributes-object>`__ for the object
    properties."""

    properties: OptionalNullable[Any] = UNSET
    """``object`` Contains edge-agnostic call-level details. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#properties-object>`__ for the object
    properties."""

    trust: OptionalNullable[Any] = UNSET
    """``object`` Contains trusted communications details including Branded Call and verified caller ID. See `Details:
    Call Summary <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#trust-object>`__ for
    the object properties."""

    annotation: OptionalNullable[Any] = UNSET
    """``object`` Programmatically labeled annotations for the Call. Developers can update the Call Summary records with
    Annotation during or after a Call. Annotations can be updated as long as the Call Summary record is addressable via
    the API. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#annotation-object>`__ for the object
    properties."""


class InsightsV1CallSummaryDict(TypedDict):
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    call_type: NotRequired[SummaryEnumCallTypeOrStr]
    call_state: NotRequired[SummaryEnumCallStateOrStr]
    answered_by: NotRequired[SummaryEnumAnsweredByOrStr]
    processing_state: NotRequired[SummaryEnumProcessingStateOrStr]
    created_time: NotRequired[RFC3339DateTime | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration: NotRequired[int | None]
    connect_duration: NotRequired[int | None]
    from_: NotRequired[Any | None]
    to: NotRequired[Any | None]
    carrier_edge: NotRequired[Any | None]
    client_edge: NotRequired[Any | None]
    sdk_edge: NotRequired[Any | None]
    sip_edge: NotRequired[Any | None]
    tags: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
    attributes: NotRequired[Any | None]
    properties: NotRequired[Any | None]
    trust: NotRequired[Any | None]
    annotation: NotRequired[Any | None]
