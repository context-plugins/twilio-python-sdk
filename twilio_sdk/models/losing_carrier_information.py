from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.customer_type import CustomerTypeOrStr


class LosingCarrierInformation(SdkBaseModel):
    customer_name: str
    """Customer name as it is registered with the losing carrier. This can be an individual or a business name depending
    on the customer type selected."""

    account_number: Optional[str] = UNSET
    """The account number of the customer for the losing carrier. Only require for mobile phone numbers."""

    account_telephone_number: Optional[str] = UNSET
    """The account phone number of the customer for the losing carrier."""

    address_sid: Optional[str] = UNSET
    """If you already have an Address SID that represents the address needed for the LOA, you can provide an Address SID
    instead of providing the address object in the request body. This will copy the address into the port in request. If
    changes are made to the Address SID after port in request creation, those changes will not be reflected in the port
    in request."""

    address: Optional[Address] = UNSET
    authorized_representative: str
    """The first and last name of the person listed with the losing carrier who is authorized to make changes on the
    account."""

    authorized_representative_email: EmailStr
    """Email address of the person (owner of the number) who will sign the letter of authorization for the port in
    request. This email address should belong to the person named in as the authorized representative."""

    customer_type: Optional[CustomerTypeOrStr] = UNSET
    """The type of customer account in the losing carrier. This should either be: 'Individual' or 'Business'."""

    authorized_representative_katakana: Optional[str] = UNSET
    sub_municipality: Optional[str] = UNSET
    building: Optional[str] = UNSET
    katakana_name: Optional[str] = UNSET


class LosingCarrierInformationDict(TypedDict):
    customer_name: str
    account_number: NotRequired[str]
    account_telephone_number: NotRequired[str]
    address_sid: NotRequired[str]
    address: NotRequired[Address | AddressDict]
    authorized_representative: str
    authorized_representative_email: EmailStr
    customer_type: NotRequired[CustomerTypeOrStr]
    authorized_representative_katakana: NotRequired[str]
    sub_municipality: NotRequired[str]
    building: NotRequired[str]
    katakana_name: NotRequired[str]
