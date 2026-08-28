from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IncomingPhoneNumberAssignedAddOnExtension(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the resource."""

    resource_sid: OptionalNullable[str] = UNSET
    """The SID of the Phone Number to which the Add-on is assigned."""

    assigned_add_on_sid: OptionalNullable[str] = UNSET
    """The SID that uniquely identifies the assigned Add-on installation."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    product_name: OptionalNullable[str] = UNSET
    """A string that you assigned to describe the Product this Extension is used within."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used in place of the resource's
    ``sid`` in the URL to address the resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    enabled: OptionalNullable[bool] = UNSET
    """Whether the Extension will be invoked."""


class IncomingPhoneNumberAssignedAddOnExtensionDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    resource_sid: NotRequired[str | None]
    assigned_add_on_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    product_name: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    uri: NotRequired[str | None]
    enabled: NotRequired[bool | None]
