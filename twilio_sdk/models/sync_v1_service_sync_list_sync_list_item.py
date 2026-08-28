from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SyncV1ServiceSyncListSyncListItem(SdkBaseModel):
    index: Optional[int] = UNSET
    """The automatically generated index of the List Item. The ``index`` values of the List Items in a Sync List can
    have gaps in their sequence."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the List Item resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ the resource is associated
    with."""

    list_sid: OptionalNullable[str] = UNSET
    """The SID of the Sync List that contains the List Item."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the List Item resource."""

    revision: OptionalNullable[str] = UNSET
    """The current revision of the item, represented as a string."""

    data: OptionalNullable[Any] = UNSET
    """An arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length."""

    date_expires: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the List Item expires and will be deleted, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format. If the List Item does not expire, this value is ``null``. The
    List Item resource might not be deleted immediately after it expires."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    created_by: OptionalNullable[str] = UNSET
    """The identity of the List Item's creator. If the item is created from the client SDK, the value matches the Access
    Token's ``identity`` field. If the item was created from the REST API, the value is ``system``."""


class SyncV1ServiceSyncListSyncListItemDict(TypedDict):
    index: NotRequired[int]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    list_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    revision: NotRequired[str | None]
    data: NotRequired[Any | None]
    date_expires: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    created_by: NotRequired[str | None]
