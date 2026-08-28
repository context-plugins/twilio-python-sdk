from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import (
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn,
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnDict,
)


class ListIncomingPhoneNumberAssignedAddOnResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    assigned_add_ons: Optional[list[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn]] = UNSET


class ListIncomingPhoneNumberAssignedAddOnResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    assigned_add_ons: NotRequired[
        list[
            (
                ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
                | ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnDict
            )
        ]
    ]
