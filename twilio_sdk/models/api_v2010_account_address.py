from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountAddress(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible for the Address
    resource."""

    city: OptionalNullable[str] = UNSET
    """The city in which the address is located."""

    customer_name: OptionalNullable[str] = UNSET
    """The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte
    characters."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    iso_country: OptionalNullable[str] = UNSET
    """The ISO country code of the address."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code of the address."""

    region: OptionalNullable[str] = UNSET
    """The state or region of the address."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Address resource."""

    street: OptionalNullable[str] = UNSET
    """The number and street address of the address."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    emergency_enabled: OptionalNullable[bool] = UNSET
    """Whether emergency calling has been enabled on this number."""

    validated: OptionalNullable[bool] = UNSET
    """Whether the address has been validated to comply with local regulation. In countries that require valid
    addresses, an invalid address will not be accepted. ``true`` indicates the Address has been validated. ``false``
    indicate the country doesn't require validation or the Address is not valid."""

    verified: OptionalNullable[bool] = UNSET
    """Whether the address has been verified to comply with regulation. In countries that require valid addresses, an
    invalid address will not be accepted. ``true`` indicates the Address has been verified. ``false`` indicate the
    country doesn't require verified or the Address is not valid."""

    street_secondary: OptionalNullable[str] = UNSET
    """The additional number and street address of the address."""


class ApiV2010AccountAddressDict(TypedDict):
    account_sid: NotRequired[str | None]
    city: NotRequired[str | None]
    customer_name: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    iso_country: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    region: NotRequired[str | None]
    sid: NotRequired[str | None]
    street: NotRequired[str | None]
    uri: NotRequired[str | None]
    emergency_enabled: NotRequired[bool | None]
    validated: NotRequired[bool | None]
    verified: NotRequired[bool | None]
    street_secondary: NotRequired[str | None]
