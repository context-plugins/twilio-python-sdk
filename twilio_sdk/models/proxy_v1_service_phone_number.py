from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .capabilities import Capabilities, CapabilitiesDict


class ProxyV1ServicePhoneNumber(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the PhoneNumber resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the PhoneNumber
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the PhoneNumber resource's parent `Service <https://www.twilio.com/docs/proxy/api/service>`__
    resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    iso_country: OptionalNullable[str] = UNSET
    """The ISO Country Code for the phone number."""

    capabilities: OptionalNullable[Capabilities] = UNSET
    """The capabilities of the phone number."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the PhoneNumber resource."""

    is_reserved: OptionalNullable[bool] = UNSET
    """Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See
    `Reserved Phone Numbers <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__ for more information."""

    in_use: Optional[int] = UNSET
    """The number of open session assigned to the number. See the `How many Phone Numbers do I need?
    <https://www.twilio.com/docs/proxy/phone-numbers-needed>`__ guide for more information."""


class ProxyV1ServicePhoneNumberDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    phone_number: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    iso_country: NotRequired[str | None]
    capabilities: NotRequired[Capabilities | CapabilitiesDict | None]
    url: NotRequired[AnyUrl | None]
    is_reserved: NotRequired[bool | None]
    in_use: NotRequired[int]
