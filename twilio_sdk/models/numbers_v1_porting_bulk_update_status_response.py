from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .numbers_v1_porting_bulk_phone_number_update_detail import (
    NumbersV1PortingBulkPhoneNumberUpdateDetail,
    NumbersV1PortingBulkPhoneNumberUpdateDetailDict,
)


class NumbersV1PortingBulkUpdateStatusResponse(SdkBaseModel):
    successful_updates: list[NumbersV1PortingBulkPhoneNumberUpdateDetail]
    failed_updates: list[NumbersV1PortingBulkPhoneNumberUpdateDetail]


class NumbersV1PortingBulkUpdateStatusResponseDict(TypedDict):
    successful_updates: list[
        NumbersV1PortingBulkPhoneNumberUpdateDetail | NumbersV1PortingBulkPhoneNumberUpdateDetailDict
    ]
    failed_updates: list[NumbersV1PortingBulkPhoneNumberUpdateDetail | NumbersV1PortingBulkPhoneNumberUpdateDetailDict]
