from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .phone_number_report_filter import PhoneNumberReportFilter, PhoneNumberReportFilterDict
from .time_range1 import TimeRange1, TimeRange1Dict


class InsightsV2CreatePhoneNumbersReportRequest(SdkBaseModel):
    time_range: Optional[TimeRange1] = UNSET
    filters: Optional[list[PhoneNumberReportFilter]] = UNSET
    size: Optional[int] = UNSET
    """The number of max available top Phone Numbers to generate."""


class InsightsV2CreatePhoneNumbersReportRequestDict(TypedDict):
    time_range: NotRequired[TimeRange1 | TimeRange1Dict]
    filters: NotRequired[list[PhoneNumberReportFilter | PhoneNumberReportFilterDict]]
    size: NotRequired[int]
