from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SyncV1ServiceSyncMapSyncMapItem(SdkBaseModel):
    key: OptionalNullable[str] = UNSET
    """The unique, user-defined key for the Map Item."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Map Item resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ the resource is associated
    with."""

    map_sid: OptionalNullable[str] = UNSET
    """The SID of the Sync Map that contains the Map Item."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Map Item resource."""

    revision: OptionalNullable[str] = UNSET
    """The current revision of the Map Item, represented as a string."""

    data: OptionalNullable[Any] = UNSET
    """An arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length."""

    date_expires: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Map Item expires and will be deleted, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format. If the Map Item does not expire, this value is ``null``. The Map
    Item might not be deleted immediately after it expires."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    created_by: OptionalNullable[str] = UNSET
    """The identity of the Map Item's creator. If the Map Item is created from the client SDK, the value matches the
    Access Token's ``identity`` field. If the Map Item was created from the REST API, the value is ``system``."""


class SyncV1ServiceSyncMapSyncMapItemDict(TypedDict):
    key: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    map_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    revision: NotRequired[str | None]
    data: NotRequired[Any | None]
    date_expires: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    created_by: NotRequired[str | None]
