from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SyncV1ServiceSyncMapSyncMapPermission(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Sync Map Permission
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ the resource is associated
    with."""

    map_sid: OptionalNullable[str] = UNSET
    """The SID of the Sync Map to which the Permission applies."""

    identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the resource's User within the Service to an FPA
    token."""

    read: OptionalNullable[bool] = UNSET
    """Whether the identity can read the Sync Map and its Items."""

    write: OptionalNullable[bool] = UNSET
    """Whether the identity can create, update, and delete Items in the Sync Map."""

    manage: OptionalNullable[bool] = UNSET
    """Whether the identity can delete the Sync Map."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Sync Map Permission resource."""


class SyncV1ServiceSyncMapSyncMapPermissionDict(TypedDict):
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    map_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    read: NotRequired[bool | None]
    write: NotRequired[bool | None]
    manage: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
