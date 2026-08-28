from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.recording_transcription_enum_status import RecordingTranscriptionEnumStatusOrStr


class ApiV2010AccountRecordingRecordingTranscription(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Transcription
    resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create the transcription."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    duration: OptionalNullable[str] = UNSET
    """The duration of the transcribed audio in seconds."""

    price: OptionalNullable[float] = UNSET
    """The charge for the transcript in the currency associated with the account. This value is populated after the
    transcript is complete so it may not be available immediately."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency in which ``price`` is measured, in `ISO 4127
    <https://www.iso.org/iso/home/standards/currency_codes.htm>`__ format (e.g. ``usd``, ``eur``, ``jpy``)."""

    recording_sid: OptionalNullable[str] = UNSET
    """The SID of the `Recording <https://www.twilio.com/docs/voice/api/recording>`__ from which the transcription was
    created."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Transcription resource."""

    status: Optional[RecordingTranscriptionEnumStatusOrStr] = UNSET
    """The status of the transcription. Can be: ``in-progress``, ``completed``, ``failed``."""

    transcription_text: OptionalNullable[str] = UNSET
    """The text content of the transcription."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The transcription type."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountRecordingRecordingTranscriptionDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    duration: NotRequired[str | None]
    price: NotRequired[float | None]
    price_unit: NotRequired[str | None]
    recording_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    status: NotRequired[RecordingTranscriptionEnumStatusOrStr]
    transcription_text: NotRequired[str | None]
    type_: NotRequired[str | None]
    uri: NotRequired[str | None]
