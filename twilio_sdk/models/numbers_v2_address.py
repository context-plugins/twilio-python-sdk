from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class NumbersV2Address(SdkBaseModel):
    sid: Optional[str] = UNSET
    """A 34 character string that uniquely identifies this Address resource."""

    account_sid: Optional[str] = UNSET
    """The unique SID identifier of the Account."""

    customer_name: OptionalNullable[str] = UNSET
    """The name of the customer associated with this address."""

    date_created: Optional[RFC3339DateTime] = UNSET
    """The date that this resource was created, given in RFC 2822 format."""

    date_updated: Optional[RFC3339DateTime] = UNSET
    """The date that this resource was last updated, given in RFC 2822 format."""

    emergency_enabled: Optional[bool] = UNSET
    """Whether this address is enabled for emergency services."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description of this resource, up to 64 characters."""

    iso_country: Optional[str] = UNSET
    """The ISO country code of this address."""

    locality: OptionalNullable[str] = UNSET
    """The locality or city of this address."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code of this address."""

    region: OptionalNullable[str] = UNSET
    """The state or region of this address."""

    source: Optional[str] = UNSET
    """The source system that created this address."""

    status: Optional[str] = UNSET
    """The status of this address."""

    street: OptionalNullable[str] = UNSET
    """The street address."""

    street_secondary: OptionalNullable[str] = UNSET
    """The additional street address information."""

    subresource_uris: Optional[Any] = UNSET
    """A list of related resources identified by their URIs."""

    validated: Optional[bool] = UNSET
    """Whether this address has been validated."""

    verified: Optional[bool] = UNSET
    """Whether this address has been verified."""


class NumbersV2AddressDict(TypedDict):
    sid: NotRequired[str]
    account_sid: NotRequired[str]
    customer_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime]
    date_updated: NotRequired[RFC3339DateTime]
    emergency_enabled: NotRequired[bool]
    friendly_name: NotRequired[str | None]
    iso_country: NotRequired[str]
    locality: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    region: NotRequired[str | None]
    source: NotRequired[str]
    status: NotRequired[str]
    street: NotRequired[str | None]
    street_secondary: NotRequired[str | None]
    subresource_uris: NotRequired[Any]
    validated: NotRequired[bool]
    verified: NotRequired[bool]
