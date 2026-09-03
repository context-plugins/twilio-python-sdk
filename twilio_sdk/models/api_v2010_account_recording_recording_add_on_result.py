from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.recording_add_on_result_enum_status import RecordingAddOnResultEnumStatusOrStr


class ApiV2010AccountRecordingRecordingAddOnResult(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Recording AddOnResult resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Recording AddOnResult
    resource."""

    status: Optional[RecordingAddOnResultEnumStatusOrStr] = UNSET
    """The status of the result. Can be: ``canceled``, ``completed``, ``deleted``, ``failed``, ``in-progress``,
    ``init``, ``processing``, ``queued``."""

    add_on_sid: OptionalNullable[str] = UNSET
    """The SID of the Add-on to which the result belongs."""

    add_on_configuration_sid: OptionalNullable[str] = UNSET
    """The SID of the Add-on configuration."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_completed: OptionalNullable[str] = UNSET
    """The date and time in GMT that the result was completed specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    reference_sid: OptionalNullable[str] = UNSET
    """The SID of the recording to which the AddOnResult resource belongs."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their relative URIs."""


class ApiV2010AccountRecordingRecordingAddOnResultDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    status: NotRequired[RecordingAddOnResultEnumStatusOrStr]
    add_on_sid: NotRequired[str | None]
    add_on_configuration_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    date_completed: NotRequired[str | None]
    reference_sid: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
