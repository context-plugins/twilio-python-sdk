from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.conference_recording_enum_source import ConferenceRecordingEnumSourceOrStr
from .enums.conference_recording_enum_status import ConferenceRecordingEnumStatusOrStr


class ApiV2010AccountConferenceConferenceRecording(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Conference Recording
    resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create the recording."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Conference Recording resource
    is associated with."""

    conference_sid: OptionalNullable[str] = UNSET
    """The Conference SID that identifies the conference associated with the recording."""

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
    """The unique string that that we created to identify the Conference Recording resource."""

    price: OptionalNullable[str] = UNSET
    """The one-time cost of creating the recording in the ``price_unit`` currency."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency used in the ``price`` property. Example: ``USD``."""

    status: Optional[ConferenceRecordingEnumStatusOrStr] = UNSET
    """The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed statuses on
    in-progress recordings, check out how to `Update a Recording Resource
    <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__."""

    channels: Optional[int] = UNSET
    """The number of channels in the final recording file. Can be: ``1``, or ``2``. Separating a two leg call into two
    separate channels of the recording file is supported in `Dial
    <https://www.twilio.com/docs/voice/twiml/dial#attributes-record>`__ and `Outbound Rest API
    <https://www.twilio.com/docs/voice/make-calls>`__ record options."""

    source: Optional[ConferenceRecordingEnumSourceOrStr] = UNSET
    """How the recording was created. Can be: ``DialVerb``, ``Conference``, ``OutboundAPI``, ``Trunking``,
    ``RecordVerb``, ``StartCallRecordingAPI``, ``StartConferenceRecordingAPI``."""

    error_code: OptionalNullable[int] = UNSET
    """The error code that describes why the recording is ``absent``. The error code is described in our `Error
    Dictionary <https://www.twilio.com/docs/api/errors>`__. This value is null if the recording ``status`` is not
    ``absent``."""

    encryption_details: OptionalNullable[Any] = UNSET
    """How to decrypt the recording if it was encrypted using `Call Recording Encryption
    <https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption>`__ feature."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountConferenceConferenceRecordingDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    conference_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    start_time: NotRequired[str | None]
    duration: NotRequired[str | None]
    sid: NotRequired[str | None]
    price: NotRequired[str | None]
    price_unit: NotRequired[str | None]
    status: NotRequired[ConferenceRecordingEnumStatusOrStr]
    channels: NotRequired[int]
    source: NotRequired[ConferenceRecordingEnumSourceOrStr]
    error_code: NotRequired[int | None]
    encryption_details: NotRequired[Any | None]
    uri: NotRequired[str | None]
