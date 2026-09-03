from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.realtime_transcription_enum_status import RealtimeTranscriptionEnumStatusOrStr


class ApiV2010AccountCallRealtimeTranscription(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The SID of the Transcription resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this Transcription
    resource."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription resource is
    associated with."""

    name: OptionalNullable[str] = UNSET
    """The user-specified name of this Transcription, if one was given when the Transcription was created. This may be
    used to stop the Transcription."""

    status: Optional[RealtimeTranscriptionEnumStatusOrStr] = UNSET
    """The status - one of ``stopped``, ``in-flight``"""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    uri: OptionalNullable[str] = UNSET


class ApiV2010AccountCallRealtimeTranscriptionDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    status: NotRequired[RealtimeTranscriptionEnumStatusOrStr]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
