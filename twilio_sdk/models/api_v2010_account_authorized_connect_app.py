from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.authorized_connect_app_enum_permission import AuthorizedConnectAppEnumPermissionOrStr


class ApiV2010AccountAuthorizedConnectApp(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the AuthorizedConnectApp
    resource."""

    connect_app_company_name: OptionalNullable[str] = UNSET
    """The company name set for the Connect App."""

    connect_app_description: OptionalNullable[str] = UNSET
    """A detailed description of the Connect App."""

    connect_app_friendly_name: OptionalNullable[str] = UNSET
    """The name of the Connect App."""

    connect_app_homepage_url: OptionalNullable[str] = UNSET
    """The public URL for the Connect App."""

    connect_app_sid: OptionalNullable[str] = UNSET
    """The SID that we assigned to the Connect App."""

    permissions: Optional[list[AuthorizedConnectAppEnumPermissionOrStr | None]] = UNSET
    """The set of permissions that you authorized for the Connect App. Can be: ``get-all`` or ``post-all``."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountAuthorizedConnectAppDict(TypedDict):
    account_sid: NotRequired[str | None]
    connect_app_company_name: NotRequired[str | None]
    connect_app_description: NotRequired[str | None]
    connect_app_friendly_name: NotRequired[str | None]
    connect_app_homepage_url: NotRequired[str | None]
    connect_app_sid: NotRequired[str | None]
    permissions: NotRequired[list[AuthorizedConnectAppEnumPermissionOrStr | None]]
    uri: NotRequired[str | None]
