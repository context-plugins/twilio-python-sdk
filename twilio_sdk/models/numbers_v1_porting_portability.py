from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.porting_portability_enum_number_type import PortingPortabilityEnumNumberTypeOrStr


class NumbersV1PortingPortability(SdkBaseModel):
    phone_number: OptionalNullable[str] = UNSET
    """The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212)."""

    account_sid: OptionalNullable[str] = UNSET
    """Account Sid that the phone number belongs to in Twilio. This is only returned for phone numbers that already
    exist in Twilio’s inventory and belong to your account or sub account."""

    portable: OptionalNullable[bool] = UNSET
    """Boolean flag indicates if the phone number can be ported into Twilio through the Porting API or not."""

    pin_and_account_number_required: OptionalNullable[bool] = UNSET
    """Indicates if the port in process will require a personal identification number (PIN) and an account number for
    this phone number. If this is true you will be required to submit both a PIN and account number from the losing
    carrier for this number when opening a port in request. These fields will be required in order to complete the port
    in process to Twilio."""

    not_portable_reason: OptionalNullable[str] = UNSET
    """Reason why the phone number cannot be ported into Twilio, ``null`` otherwise."""

    not_portable_reason_code: OptionalNullable[int] = UNSET
    """The Portability Reason Code for the phone number if it cannot be ported into Twilio, ``null`` otherwise."""

    number_type: Optional[PortingPortabilityEnumNumberTypeOrStr] = UNSET
    """The type of the requested phone number. One of ``LOCAL``, ``UNKNOWN``, ``MOBILE``, ``TOLL-FREE``."""

    country: OptionalNullable[str] = UNSET
    """Country the phone number belongs to."""

    url: OptionalNullable[AnyUrl] = UNSET
    """This is the url of the request that you're trying to reach out to locate the resource."""


class NumbersV1PortingPortabilityDict(TypedDict):
    phone_number: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    portable: NotRequired[bool | None]
    pin_and_account_number_required: NotRequired[bool | None]
    not_portable_reason: NotRequired[str | None]
    not_portable_reason_code: NotRequired[int | None]
    number_type: NotRequired[PortingPortabilityEnumNumberTypeOrStr]
    country: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
