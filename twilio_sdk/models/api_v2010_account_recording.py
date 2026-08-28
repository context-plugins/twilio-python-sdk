from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.recording_enum_source import RecordingEnumSourceOrStr
from .enums.recording_enum_status import RecordingEnumStatusOrStr


class ApiV2010AccountRecording(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Recording resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used during the recording."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Recording resource is
    associated with. This will always refer to the parent leg of a two-leg call."""

    conference_sid: OptionalNullable[str] = UNSET
    """The Conference SID that identifies the conference associated with the recording, if a conference recording."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    start_time: OptionalNullable[str] = UNSET
    """The start time of the recording in GMT and in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    duration: OptionalNullable[str] = UNSET
    """The length of the recording in seconds."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Recording resource."""

    price: OptionalNullable[str] = UNSET
    """The one-time cost of creating the recording in the ``price_unit`` currency."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency used in the ``price`` property. Example: ``USD``."""

    status: Optional[RecordingEnumStatusOrStr] = UNSET
    """The status of the recording. Can be: ``processing``, ``completed``, ``absent`` or ``deleted``. For information
    about more detailed statuses on in-progress recordings, check out how to `Update a Recording Resource
    <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__."""

    channels: OptionalNullable[int] = UNSET
    """The number of channels in the recording resource. For information on specifying the number of channels in the
    downloaded recording file, check out `Fetch a Recording’s media file
    <https://www.twilio.com/docs/voice/api/recording#download-dual-channel-media-file>`__."""

    source: Optional[RecordingEnumSourceOrStr] = UNSET
    """How the recording was created. Can be: ``DialVerb``, ``Conference``, ``OutboundAPI``, ``Trunking``,
    ``RecordVerb``, ``StartCallRecordingAPI``, and ``StartConferenceRecordingAPI``."""

    error_code: OptionalNullable[int] = UNSET
    """The error code that describes why the recording is ``absent``. The error code is described in our `Error
    Dictionary <https://www.twilio.com/docs/api/errors>`__. This value is null if the recording ``status`` is not
    ``absent``."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    encryption_details: OptionalNullable[Any] = UNSET
    """How to decrypt the recording if it was encrypted using `Call Recording Encryption
    <https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption>`__ feature."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their relative URIs."""

    media_url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the media file associated with this recording resource. When stored externally, this is the full URL
    location of the media file."""


class ApiV2010AccountRecordingDict(TypedDict):
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
    status: NotRequired[RecordingEnumStatusOrStr]
    channels: NotRequired[int | None]
    source: NotRequired[RecordingEnumSourceOrStr]
    error_code: NotRequired[int | None]
    uri: NotRequired[str | None]
    encryption_details: NotRequired[Any | None]
    subresource_uris: NotRequired[Any | None]
    media_url: NotRequired[AnyUrl | None]
