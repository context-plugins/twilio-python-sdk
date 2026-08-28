from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountAvailablePhoneNumberCountry(SdkBaseModel):
    country_code: OptionalNullable[str] = UNSET
    """The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country."""

    country: OptionalNullable[str] = UNSET
    """The name of the country."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the Country resource, relative to ``https://api.twilio.com``."""

    beta: OptionalNullable[bool] = UNSET
    """Whether all phone numbers available in the country are new to the Twilio platform. ``true`` if they are and
    ``false`` if all numbers are not in the Twilio Phone Number Beta program."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related AvailablePhoneNumber resources identified by their URIs relative to
    ``https://api.twilio.com``."""


class ApiV2010AccountAvailablePhoneNumberCountryDict(TypedDict):
    country_code: NotRequired[str | None]
    country: NotRequired[str | None]
    uri: NotRequired[str | None]
    beta: NotRequired[bool | None]
    subresource_uris: NotRequired[Any | None]
