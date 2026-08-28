from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import (
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn,
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnDict,
)


class ListIncomingPhoneNumberAssignedAddOnResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    assigned_add_ons: Optional[list[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn]] = UNSET


class ListIncomingPhoneNumberAssignedAddOnResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    assigned_add_ons: NotRequired[
        list[
            (
                ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
                | ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnDict
            )
        ]
    ]
