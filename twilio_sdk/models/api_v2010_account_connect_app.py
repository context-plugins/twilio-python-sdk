from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.connect_app_enum_permission import ConnectAppEnumPermissionOrStr
from .enums.deauthorize_callback_method import DeauthorizeCallbackMethodOrStr


class ApiV2010AccountConnectApp(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the ConnectApp resource."""

    authorize_redirect_url: OptionalNullable[str] = UNSET
    """The URL we redirect the user to after we authenticate the user and obtain authorization to access the Connect
    App."""

    company_name: OptionalNullable[str] = UNSET
    """The company name set for the Connect App."""

    deauthorize_callback_method: OptionalNullable[DeauthorizeCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``deauthorize_callback_url``."""

    deauthorize_callback_url: OptionalNullable[str] = UNSET
    """The URL we call using the ``deauthorize_callback_method`` to de-authorize the Connect App."""

    description: OptionalNullable[str] = UNSET
    """The description of the Connect App."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    homepage_url: OptionalNullable[str] = UNSET
    """The public URL where users can obtain more information about this Connect App."""

    permissions: Optional[list[ConnectAppEnumPermissionOrStr | None]] = UNSET
    """The set of permissions that your ConnectApp requests."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the ConnectApp resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountConnectAppDict(TypedDict):
    account_sid: NotRequired[str | None]
    authorize_redirect_url: NotRequired[str | None]
    company_name: NotRequired[str | None]
    deauthorize_callback_method: NotRequired[DeauthorizeCallbackMethodOrStr | None]
    deauthorize_callback_url: NotRequired[str | None]
    description: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    homepage_url: NotRequired[str | None]
    permissions: NotRequired[list[ConnectAppEnumPermissionOrStr | None]]
    sid: NotRequired[str | None]
    uri: NotRequired[str | None]
