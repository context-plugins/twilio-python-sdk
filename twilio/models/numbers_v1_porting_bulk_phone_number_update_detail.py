from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV1PortingBulkPhoneNumberUpdateDetail(SdkBaseModel):
    port_in_phone_number_sid: str
    current_status: str
    requested_status: str
    error_message: OptionalNullable[str] = UNSET
    """Error message explaining why the update failed"""


class NumbersV1PortingBulkPhoneNumberUpdateDetailDict(TypedDict):
    port_in_phone_number_sid: str
    current_status: str
    requested_status: str
    error_message: NotRequired[str | None]
