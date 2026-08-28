from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .call_summary_crelay_interruptions import CallSummaryCrelayInterruptions, CallSummaryCrelayInterruptionsDict
from .call_summary_crelay_rate_stats import CallSummaryCrelayRateStats, CallSummaryCrelayRateStatsDict
from .call_summary_crelay_token_stats import CallSummaryCrelayTokenStats, CallSummaryCrelayTokenStatsDict
from .call_summary_crelay_word_stats import CallSummaryCrelayWordStats, CallSummaryCrelayWordStatsDict
from .enums.call_summary_crelay_session_state import CallSummaryCrelaySessionStateOrStr


class CallSummaryAgentSessionSummary(SdkBaseModel):
    session_id: Optional[str] = UNSET
    tts_latency_ms: Optional[CallSummaryCrelayRateStats] = UNSET
    stt_latency_ms: Optional[CallSummaryCrelayRateStats] = UNSET
    network_latency_ms: Optional[CallSummaryCrelayRateStats] = UNSET
    time_to_first_audio_ms: Optional[CallSummaryCrelayRateStats] = UNSET
    application_latency_ms: Optional[CallSummaryCrelayRateStats] = UNSET
    tokens: Optional[CallSummaryCrelayTokenStats] = UNSET
    words: Optional[CallSummaryCrelayWordStats] = UNSET
    turns: Optional[int] = UNSET
    interruptions: Optional[CallSummaryCrelayInterruptions] = UNSET
    session_state: Optional[CallSummaryCrelaySessionStateOrStr] = UNSET


class CallSummaryAgentSessionSummaryDict(TypedDict):
    session_id: NotRequired[str]
    tts_latency_ms: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
    stt_latency_ms: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
    network_latency_ms: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
    time_to_first_audio_ms: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
    application_latency_ms: NotRequired[CallSummaryCrelayRateStats | CallSummaryCrelayRateStatsDict]
    tokens: NotRequired[CallSummaryCrelayTokenStats | CallSummaryCrelayTokenStatsDict]
    words: NotRequired[CallSummaryCrelayWordStats | CallSummaryCrelayWordStatsDict]
    turns: NotRequired[int]
    interruptions: NotRequired[CallSummaryCrelayInterruptions | CallSummaryCrelayInterruptionsDict]
    session_state: NotRequired[CallSummaryCrelaySessionStateOrStr]
