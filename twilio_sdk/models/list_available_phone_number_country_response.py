from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_available_phone_number_country import (
    ApiV2010AccountAvailablePhoneNumberCountry,
    ApiV2010AccountAvailablePhoneNumberCountryDict,
)


class ListAvailablePhoneNumberCountryResponse(SdkBaseModel):
    countries: Optional[list[ApiV2010AccountAvailablePhoneNumberCountry]] = UNSET
    uri: OptionalNullable[AnyUrl] = UNSET


class ListAvailablePhoneNumberCountryResponseDict(TypedDict):
    countries: NotRequired[
        list[ApiV2010AccountAvailablePhoneNumberCountry | ApiV2010AccountAvailablePhoneNumberCountryDict]
    ]
    uri: NotRequired[AnyUrl | None]
