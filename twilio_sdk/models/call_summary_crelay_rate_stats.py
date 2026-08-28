from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallSummaryCrelayRateStats(SdkBaseModel):
    min: Optional[float] = UNSET
    max: Optional[float] = UNSET
    avg: Optional[float] = UNSET


class CallSummaryCrelayRateStatsDict(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]
    avg: NotRequired[float]
