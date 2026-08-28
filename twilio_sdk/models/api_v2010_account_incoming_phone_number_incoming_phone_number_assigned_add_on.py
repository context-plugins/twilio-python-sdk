from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the resource."""

    resource_sid: OptionalNullable[str] = UNSET
    """The SID of the Phone Number to which the Add-on is assigned."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    description: OptionalNullable[str] = UNSET
    """A short description of the functionality that the Add-on provides."""

    configuration: OptionalNullable[Any] = UNSET
    """A JSON string that represents the current configuration of this Add-on installation."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used in place of the resource's
    ``sid`` in the URL to address the resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their relative URIs."""


class ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    resource_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    description: NotRequired[str | None]
    configuration: NotRequired[Any | None]
    unique_name: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
