from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_usage_usage_record_usage_record_this_month import (
    ApiV2010AccountUsageUsageRecordUsageRecordThisMonth,
    ApiV2010AccountUsageUsageRecordUsageRecordThisMonthDict,
)


class ListUsageRecordThisMonthResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    usage_records: Optional[list[ApiV2010AccountUsageUsageRecordUsageRecordThisMonth]] = UNSET


class ListUsageRecordThisMonthResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    usage_records: NotRequired[
        list[
            (
                ApiV2010AccountUsageUsageRecordUsageRecordThisMonth
                | ApiV2010AccountUsageUsageRecordUsageRecordThisMonthDict
            )
        ]
    ]
