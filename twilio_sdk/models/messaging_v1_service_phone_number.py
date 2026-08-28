from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServicePhoneNumber(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the PhoneNumber resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the PhoneNumber
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ the resource is associated
    with."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    country_code: OptionalNullable[str] = UNSET
    """The 2-character `ISO Country Code <https://www.iso.org/iso-3166-country-codes.html>`__ of the number."""

    capabilities: Optional[list[str | None]] = UNSET
    """An array of values that describe whether the number can receive calls or messages. Can be: ``Voice``, ``SMS``,
    and ``MMS``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the PhoneNumber resource."""


class MessagingV1ServicePhoneNumberDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    phone_number: NotRequired[str | None]
    country_code: NotRequired[str | None]
    capabilities: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
