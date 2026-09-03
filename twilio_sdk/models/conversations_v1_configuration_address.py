from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1ConfigurationAddress(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ the address belongs to"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Type of Address, value can be ``whatsapp`` or ``sms``."""

    address: OptionalNullable[str] = UNSET
    """The unique address to be configured. The address can be a whatsapp address or phone number"""

    friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this configuration, limited to 256 characters. Optional."""

    auto_creation: OptionalNullable[Any] = UNSET
    """Auto Creation configuration for the address."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    url: OptionalNullable[str] = UNSET
    """An absolute API resource URL for this address configuration."""

    address_country: OptionalNullable[str] = UNSET
    """An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code
    addresses."""


class ConversationsV1ConfigurationAddressDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    type_: NotRequired[str | None]
    address: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    auto_creation: NotRequired[Any | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    address_country: NotRequired[str | None]
