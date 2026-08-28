from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .call_summary_crelay_rate_stats import CallSummaryCrelayRateStats, CallSummaryCrelayRateStatsDict


class CallSummaryCrelayTokenStats(SdkBaseModel):
    total: Optional[int] = UNSET
    tokens_per_second: Optional[CallSummaryCrelayRateStats] = UNSET


class CallSummaryCrelayTokenStatsDict(TypedDict):
    total: NotRequired[int]
    tokens_per_second: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
