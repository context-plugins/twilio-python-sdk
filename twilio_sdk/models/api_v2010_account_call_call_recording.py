from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.call_recording_enum_source import CallRecordingEnumSourceOrStr
from .enums.call_recording_enum_status import CallRecordingEnumStatusOrStr


class ApiV2010AccountCallCallRecording(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Recording resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to make the recording."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Recording resource is
    associated with."""

    conference_sid: OptionalNullable[str] = UNSET
    """The Conference SID that identifies the conference associated with the recording, if a conference recording."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    start_time: OptionalNullable[str] = UNSET
    """The start time of the recording in GMT and in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    duration: OptionalNullable[str] = UNSET
    """The length of the recording in seconds."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Recording resource."""

    price: OptionalNullable[float] = UNSET
    """The one-time cost of creating the recording in the ``price_unit`` currency."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    encryption_details: OptionalNullable[Any] = UNSET
    """How to decrypt the recording if it was encrypted using `Call Recording Encryption
    <https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption>`__ feature."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency used in the ``price`` property. Example: ``USD``."""

    status: Optional[CallRecordingEnumStatusOrStr] = UNSET
    """The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed statuses on
    in-progress recordings, check out how to `Update a Recording Resource
    <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__."""

    channels: Optional[int] = UNSET
    """The number of channels in the final recording file. Can be: ``1``, or ``2``. Separating a two leg call into two
    separate channels of the recording file is supported in `Dial
    <https://www.twilio.com/docs/voice/twiml/dial#attributes-record>`__ and `Outbound Rest API
    <https://www.twilio.com/docs/voice/make-calls>`__ record options."""

    source: Optional[CallRecordingEnumSourceOrStr] = UNSET
    """How the recording was created. Can be: ``DialVerb``, ``Conference``, ``OutboundAPI``, ``Trunking``,
    ``RecordVerb``, ``StartCallRecordingAPI``, and ``StartConferenceRecordingAPI``."""

    error_code: OptionalNullable[int] = UNSET
    """The error code that describes why the recording is ``absent``. The error code is described in our `Error
    Dictionary <https://www.twilio.com/docs/api/errors>`__. This value is null if the recording ``status`` is not
    ``absent``."""

    track: OptionalNullable[str] = UNSET
    """The recorded track. Can be: ``inbound``, ``outbound``, or ``both``."""


class ApiV2010AccountCallCallRecordingDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    conference_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    start_time: NotRequired[str | None]
    duration: NotRequired[str | None]
    sid: NotRequired[str | None]
    price: NotRequired[float | None]
    uri: NotRequired[str | None]
    encryption_details: NotRequired[Any | None]
    price_unit: NotRequired[str | None]
    status: NotRequired[CallRecordingEnumStatusOrStr]
    channels: NotRequired[int]
    source: NotRequired[CallRecordingEnumSourceOrStr]
    error_code: NotRequired[int | None]
    track: NotRequired[str | None]
