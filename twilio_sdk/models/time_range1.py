from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class TimeRange1(SdkBaseModel):
    start_datetime: Optional[RFC3339DateTime] = UNSET
    """Start date time of the report"""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """End date time of the report"""


class TimeRange1Dict(TypedDict):
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
