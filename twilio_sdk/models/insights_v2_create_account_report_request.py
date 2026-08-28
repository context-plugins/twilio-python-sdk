from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report_filter import ReportFilter, ReportFilterDict
from .time_range import TimeRange, TimeRangeDict


class InsightsV2CreateAccountReportRequest(SdkBaseModel):
    time_range: Optional[TimeRange] = UNSET
    """Optional start and end date time for the report window. Defaults to the most recent 7 days when omitted."""

    filters: Optional[list[ReportFilter]] = UNSET


class InsightsV2CreateAccountReportRequestDict(TypedDict):
    time_range: NotRequired[TimeRange | TimeRangeDict]
    filters: NotRequired[list[ReportFilter | ReportFilterDict]]
