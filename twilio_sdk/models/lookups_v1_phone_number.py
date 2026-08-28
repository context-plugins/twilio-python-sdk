from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LookupsV1PhoneNumber(SdkBaseModel):
    caller_name: OptionalNullable[Any] = UNSET
    """The name of the phone number's owner. If ``null``, that information was not available."""

    country_code: OptionalNullable[str] = UNSET
    """The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ for the phone number."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    national_format: OptionalNullable[str] = UNSET
    """The phone number, in national format."""

    carrier: OptionalNullable[Any] = UNSET
    """The telecom company that provides the phone number."""

    add_ons: OptionalNullable[Any] = UNSET
    """A JSON string with the results of the Add-ons you specified in the ``add_ons`` parameters. For the format of the
    object, see `Using Add-ons <https://www.twilio.com/docs/add-ons>`__."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class LookupsV1PhoneNumberDict(TypedDict):
    caller_name: NotRequired[Any | None]
    country_code: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    national_format: NotRequired[str | None]
    carrier: NotRequired[Any | None]
    add_ons: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
