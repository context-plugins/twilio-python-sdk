from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_available_phone_number_country_available_phone_number_mobile import (
    ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberMobile,
    ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberMobileDict,
)


class ListAvailablePhoneNumberMobileResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    available_phone_numbers: Optional[
        list[ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberMobile]
    ] = UNSET


class ListAvailablePhoneNumberMobileResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    available_phone_numbers: NotRequired[
        list[
            (
                ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberMobile
                | ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberMobileDict
            )
        ]
    ]
