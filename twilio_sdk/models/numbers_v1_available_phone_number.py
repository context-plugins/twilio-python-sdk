from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .billing import Billing, BillingDict
from .capabilities1 import Capabilities1, Capabilities1Dict
from .certifications import Certifications, CertificationsDict
from .flags import Flags, FlagsDict
from .geography import Geography, GeographyDict


class NumbersV1AvailablePhoneNumber(SdkBaseModel):
    did: OptionalNullable[str] = Field(default=UNSET, alias="Did")
    """The phone number in E.164 format."""

    inventory_did_sid: OptionalNullable[str] = Field(default=UNSET, alias="InventoryDidSid")
    """The unique string that identifies the inventory DID resource."""

    friendly_name: OptionalNullable[str] = Field(default=UNSET, alias="FriendlyName")
    """A human-readable phone number in national format."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of phone number. Can be Local, Mobile, TollFree, etc."""

    npa: OptionalNullable[str] = Field(default=UNSET, alias="Npa")
    """The North American Numbering Plan (NANP) area code of the phone number."""

    nxx: OptionalNullable[str] = Field(default=UNSET, alias="Nxx")
    """The three-digit exchange code of the phone number."""

    locked: OptionalNullable[bool] = Field(default=UNSET, alias="Locked")
    """Whether the phone number is locked for purchase."""

    locked_until: OptionalNullable[int] = Field(default=UNSET, alias="LockedUntil")
    """The Unix timestamp when the phone number lock expires."""

    capabilities: OptionalNullable[Capabilities1] = Field(default=UNSET, alias="Capabilities")
    """The set of Boolean properties that describes the SMS, MMS, Voice, and Fax capabilities of the phone number."""

    geography: OptionalNullable[Geography] = Field(default=UNSET, alias="Geography")
    """The geographic information associated with the phone number."""

    address_requirements: OptionalNullable[str] = Field(default=UNSET, alias="AddressRequirements")
    """The type of Address resource the phone number requires."""

    certifications: OptionalNullable[Certifications] = Field(default=UNSET, alias="Certifications")
    """The certifications required for the phone number."""

    billing: OptionalNullable[Billing] = Field(default=UNSET, alias="Billing")
    """The billing information for the phone number."""

    date_created: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="DateCreated")
    """The date and time in GMT when the resource was created specified in ISO 8601 format."""

    date_updated: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="DateUpdated")
    """The date and time in GMT when the resource was last updated specified in ISO 8601 format."""

    beta: OptionalNullable[bool] = Field(default=UNSET, alias="Beta")
    """Whether the phone number is in beta."""

    voice_emergency_capable: OptionalNullable[bool] = Field(default=UNSET, alias="VoiceEmergencyCapable")
    """Whether the phone number can handle emergency calls."""

    flags: OptionalNullable[Flags] = Field(default=UNSET, alias="Flags")
    """The flags that describe the phone number features."""


class NumbersV1AvailablePhoneNumberDict(TypedDict):
    did: NotRequired[str | None]
    inventory_did_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    type_: NotRequired[str | None]
    npa: NotRequired[str | None]
    nxx: NotRequired[str | None]
    locked: NotRequired[bool | None]
    locked_until: NotRequired[int | None]
    capabilities: NotRequired[Capabilities1 | Capabilities1Dict | None]
    geography: NotRequired[Geography | GeographyDict | None]
    address_requirements: NotRequired[str | None]
    certifications: NotRequired[Certifications | CertificationsDict | None]
    billing: NotRequired[Billing | BillingDict | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    beta: NotRequired[bool | None]
    voice_emergency_capable: NotRequired[bool | None]
    flags: NotRequired[Flags | FlagsDict | None]
