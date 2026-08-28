from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IdentityMatchParameters(SdkBaseModel):
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    address_line1: Optional[str] = UNSET
    address_line2: Optional[str] = UNSET
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    postal_code: Optional[str] = UNSET
    address_country_code: Optional[str] = UNSET
    national_id: Optional[str] = UNSET
    date_of_birth: Optional[str] = UNSET


class IdentityMatchParametersDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postal_code: NotRequired[str]
    address_country_code: NotRequired[str]
    national_id: NotRequired[str]
    date_of_birth: NotRequired[str]
