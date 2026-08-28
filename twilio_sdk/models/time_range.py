from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class TimeRange(SdkBaseModel):
    """Optional start and end date time for the report window. Defaults to the most recent 7 days when omitted."""

    start_datetime: Optional[RFC3339DateTime] = UNSET
    """Start date time of the report"""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """End date time of the report"""


class TimeRangeDict(TypedDict):
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
