from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_usage_usage_record_usage_record_yesterday import (
    ApiV2010AccountUsageUsageRecordUsageRecordYesterday,
    ApiV2010AccountUsageUsageRecordUsageRecordYesterdayDict,
)


class ListUsageRecordYesterdayResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    usage_records: Optional[list[ApiV2010AccountUsageUsageRecordUsageRecordYesterday]] = UNSET


class ListUsageRecordYesterdayResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    usage_records: NotRequired[
        list[
            (
                ApiV2010AccountUsageUsageRecordUsageRecordYesterday
                | ApiV2010AccountUsageUsageRecordUsageRecordYesterdayDict
            )
        ]
    ]
