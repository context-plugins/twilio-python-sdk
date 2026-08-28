from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .email import Email, EmailDict
from .enums.use_case import UseCaseOrStr
from .phone_number import PhoneNumber, PhoneNumberDict
from .website import Website, WebsiteDict


class MessagingV2ChannelsSenderProfileGenericResponse(SdkBaseModel):
    """The profile information for the sender."""

    name: OptionalNullable[str] = UNSET
    """The name of the sender."""

    about: OptionalNullable[str] = UNSET
    """The profile about text for the sender."""

    address: OptionalNullable[str] = UNSET
    """The address of the sender."""

    description: OptionalNullable[str] = UNSET
    """The description of the sender."""

    logo_url: OptionalNullable[str] = UNSET
    """The logo URL of the sender."""

    banner_url: OptionalNullable[str] = UNSET
    """The banner URL of the sender."""

    privacy_url: OptionalNullable[str] = UNSET
    """The privacy URL of the sender. Must be a publicly accessible HTTP or HTTPS URI associated with the sender."""

    terms_of_service_url: OptionalNullable[str] = UNSET
    """The terms of service URL of the sender."""

    accent_color: OptionalNullable[str] = UNSET
    """The color theme of the sender. Must be in hex format and have at least a 4:5:1 contrast ratio against white."""

    use_case: OptionalNullable[UseCaseOrStr] = UNSET
    """The messaging use case type for the RCS sender. Allowed values are ``PROMOTIONAL``, ``TRANSACTIONAL``, ``OTP``,
    ``MULTI_USE``. Defaults to ``MULTI_USE`` if not provided. Cannot be modified after launch."""

    vertical: OptionalNullable[str] = UNSET
    """The vertical of the sender. Allowed values are:
    - ``Alcohol``
    - ``Automotive``
    - ``Beauty, Spa and Salon``
    - ``Clothing and Apparel``
    - ``Education``
    - ``Entertainment``
    - ``Event Planning and Service``
    - ``Finance and Banking``
    - ``Food and Grocery``
    - ``Hotel and Lodging``
    - ``Matrimony Service``
    - ``Medical and Health``
    - ``Non-profit``
    - ``Online Gambling``
    - ``OTC Drugs``
    - ``Other``
    - ``Physical Gambling``
    - ``Professional Services``
    - ``Public Service``
    - ``Restaurant``
    - ``Shopping and Retail``
    - ``Travel and Transportation``"""

    websites: Optional[list[Website | None]] = UNSET
    """The websites of the sender."""

    emails: Optional[list[Email | None]] = UNSET
    """The emails of the sender."""

    phone_numbers: Optional[list[PhoneNumber | None]] = UNSET
    """The phone numbers of the sender."""


class MessagingV2ChannelsSenderProfileGenericResponseDict(TypedDict):
    name: NotRequired[str | None]
    about: NotRequired[str | None]
    address: NotRequired[str | None]
    description: NotRequired[str | None]
    logo_url: NotRequired[str | None]
    banner_url: NotRequired[str | None]
    privacy_url: NotRequired[str | None]
    terms_of_service_url: NotRequired[str | None]
    accent_color: NotRequired[str | None]
    use_case: NotRequired[UseCaseOrStr | None]
    vertical: NotRequired[str | None]
    websites: NotRequired[list[Website | WebsiteDict | None]]
    emails: NotRequired[list[Email | EmailDict | None]]
    phone_numbers: NotRequired[list[PhoneNumber | PhoneNumberDict | None]]
