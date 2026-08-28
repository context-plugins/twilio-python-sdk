from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Recording AddOnResult Payload resource."""

    add_on_result_sid: OptionalNullable[str] = UNSET
    """The SID of the AddOnResult to which the payload belongs."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Recording AddOnResult
    Payload resource."""

    label: OptionalNullable[str] = UNSET
    """The string provided by the vendor that describes the payload."""

    add_on_sid: OptionalNullable[str] = UNSET
    """The SID of the Add-on to which the result belongs."""

    add_on_configuration_sid: OptionalNullable[str] = UNSET
    """The SID of the Add-on configuration."""

    content_type: OptionalNullable[str] = UNSET
    """The MIME type of the payload."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    reference_sid: OptionalNullable[str] = UNSET
    """The SID of the recording to which the AddOnResult resource that contains the payload belongs."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their relative URIs."""


class ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayloadDict(TypedDict):
    sid: NotRequired[str | None]
    add_on_result_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    label: NotRequired[str | None]
    add_on_sid: NotRequired[str | None]
    add_on_configuration_sid: NotRequired[str | None]
    content_type: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    reference_sid: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
