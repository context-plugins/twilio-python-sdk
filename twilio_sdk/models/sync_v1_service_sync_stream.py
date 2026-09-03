from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SyncV1ServiceSyncStream(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Sync Stream resource."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used in place of the resource's
    ``sid`` in the URL to address the resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Sync Stream
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ the resource is associated
    with."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Message Stream resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Stream's nested resources."""

    date_expires: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Message Stream expires and will be deleted, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format. If the Message Stream does not expire, this value is ``null``.
    The Stream might not be deleted immediately after it expires."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    created_by: OptionalNullable[str] = UNSET
    """The identity of the Stream's creator. If the Stream is created from the client SDK, the value matches the Access
    Token's ``identity`` field. If the Stream was created from the REST API, the value is 'system'."""


class SyncV1ServiceSyncStreamDict(TypedDict):
    sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
    date_expires: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    created_by: NotRequired[str | None]
