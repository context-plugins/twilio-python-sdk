from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SyncV1ServiceDocumentDocumentPermission(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Document Permission
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ the resource is associated
    with."""

    document_sid: OptionalNullable[str] = UNSET
    """The SID of the Sync Document to which the Document Permission applies."""

    identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the resource's User within the Service to an FPA
    token."""

    read: OptionalNullable[bool] = UNSET
    """Whether the identity can read the Sync Document."""

    write: OptionalNullable[bool] = UNSET
    """Whether the identity can update the Sync Document."""

    manage: OptionalNullable[bool] = UNSET
    """Whether the identity can delete the Sync Document."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Sync Document Permission resource."""


class SyncV1ServiceDocumentDocumentPermissionDict(TypedDict):
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    document_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    read: NotRequired[bool | None]
    write: NotRequired[bool | None]
    manage: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
