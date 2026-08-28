from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .report_filter import ReportFilter, ReportFilterDict


class ReportMetadata(SdkBaseModel):
    start_datetime: Optional[RFC3339DateTime] = UNSET
    """Start date time of the report"""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """End date time of the report"""

    filters: Optional[list[ReportFilter]] = UNSET
    """Filter values applied to the report"""


class ReportMetadataDict(TypedDict):
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
    filters: NotRequired[list[ReportFilter | ReportFilterDict]]
