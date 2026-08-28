from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .incoming_phone_number_assigned_add_on_extension import (
    IncomingPhoneNumberAssignedAddOnExtension,
    IncomingPhoneNumberAssignedAddOnExtensionDict,
)


class ListIncomingPhoneNumberAssignedAddOnExtensionResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    extensions: Optional[list[IncomingPhoneNumberAssignedAddOnExtension]] = UNSET


class ListIncomingPhoneNumberAssignedAddOnExtensionResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    extensions: NotRequired[
        list[IncomingPhoneNumberAssignedAddOnExtension | IncomingPhoneNumberAssignedAddOnExtensionDict]
    ]
