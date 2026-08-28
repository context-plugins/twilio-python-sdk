from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .call_summary_crelay_rate_stats import CallSummaryCrelayRateStats, CallSummaryCrelayRateStatsDict


class CallSummaryCrelayWordStats(SdkBaseModel):
    total: Optional[int] = UNSET
    words_per_minute: Optional[CallSummaryCrelayRateStats] = UNSET


class CallSummaryCrelayWordStatsDict(TypedDict):
    total: NotRequired[int]
    words_per_minute: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
