from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .capabilities import Capabilities, CapabilitiesDict


class ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberLocal(SdkBaseModel):
    friendly_name: OptionalNullable[str] = UNSET
    """A formatted version of the phone number."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    lata: OptionalNullable[str] = UNSET
    """The `LATA <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__ of this phone number. Available for
    only phone numbers from the US and Canada."""

    locality: OptionalNullable[str] = UNSET
    """The locality or city of this phone number's location."""

    rate_center: OptionalNullable[str] = UNSET
    """The `rate center <https://en.wikipedia.org/wiki/Telephone_exchange>`__ of this phone number. Available for only
    phone numbers from the US and Canada."""

    latitude: OptionalNullable[float] = UNSET
    """The latitude of this phone number's location. Available for only phone numbers from the US and Canada."""

    longitude: OptionalNullable[float] = UNSET
    """The longitude of this phone number's location. Available for only phone numbers from the US and Canada."""

    region: OptionalNullable[str] = UNSET
    """The two-letter state or province abbreviation of this phone number's location. Available for only phone numbers
    from the US and Canada."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal or ZIP code of this phone number's location. Available for only phone numbers from the US and
    Canada."""

    iso_country: OptionalNullable[str] = UNSET
    """The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of this phone number."""

    address_requirements: OptionalNullable[str] = UNSET
    """The type of `Address <https://www.twilio.com/docs/usage/api/address>`__ resource the phone number requires. Can
    be: ``none``, ``any``, ``local``, or ``foreign``. ``none`` means no address is required. ``any`` means an address is
    required, but it can be anywhere in the world. ``local`` means an address in the phone number's country is required.
    ``foreign`` means an address outside of the phone number's country is required."""

    beta: OptionalNullable[bool] = UNSET
    """Whether the phone number is new to the Twilio platform. Can be: ``true`` or ``false``."""

    capabilities: OptionalNullable[Capabilities] = UNSET
    """The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities
    are: ``Voice``, ``SMS``, and ``MMS`` and each capability can be: ``true`` or ``false``."""


class ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberLocalDict(TypedDict):
    friendly_name: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    lata: NotRequired[str | None]
    locality: NotRequired[str | None]
    rate_center: NotRequired[str | None]
    latitude: NotRequired[float | None]
    longitude: NotRequired[float | None]
    region: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    iso_country: NotRequired[str | None]
    address_requirements: NotRequired[str | None]
    beta: NotRequired[bool | None]
    capabilities: NotRequired[Capabilities | CapabilitiesDict | None]
