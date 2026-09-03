from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV2AddressCreate(SdkBaseModel):
    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description of this resource, up to 64 characters."""

    customer_name: OptionalNullable[str] = UNSET
    """The name of the customer associated with this address."""

    street: str
    """The street address."""

    street_secondary: OptionalNullable[str] = UNSET
    """The additional street address information."""

    locality: OptionalNullable[str] = UNSET
    """The locality or city of this address."""

    region: OptionalNullable[str] = UNSET
    """The state or region of this address."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code of this address."""

    iso_country: str
    """The ISO country code of this address."""

    source: OptionalNullable[str] = UNSET
    """The source system that created this address."""

    force_validation: OptionalNullable[bool] = UNSET
    """Whether to force validation of the address."""

    bypass_validation: OptionalNullable[bool] = UNSET
    """Whether to bypass validation of the address."""

    auto_correct_address: OptionalNullable[bool] = UNSET
    """Whether to automatically correct the address."""

    emergency_enabled: OptionalNullable[bool] = UNSET
    """Whether this address is enabled for emergency services."""


class NumbersV2AddressCreateDict(TypedDict):
    friendly_name: NotRequired[str | None]
    customer_name: NotRequired[str | None]
    street: str
    street_secondary: NotRequired[str | None]
    locality: NotRequired[str | None]
    region: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    iso_country: str
    source: NotRequired[str | None]
    force_validation: NotRequired[bool | None]
    bypass_validation: NotRequired[bool | None]
    auto_correct_address: NotRequired[bool | None]
    emergency_enabled: NotRequired[bool | None]
