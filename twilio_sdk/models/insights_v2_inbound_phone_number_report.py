from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .call_state_percentage import CallStatePercentage, CallStatePercentageDict


class InsightsV2InboundPhoneNumberReport(SdkBaseModel):
    handle: Optional[str] = UNSET
    """Inbound phone number handle represented in the report."""

    total_calls: Optional[int] = UNSET
    """Total number of calls made with the given handle during the report period."""

    call_answer_score: Optional[float] = UNSET
    """The call answer score measures customers behavior to the delivered calls. The score is a value between 0 and 100,
    where 100 indicates that all calls were successfully answered."""

    call_state_percentage: Optional[CallStatePercentage] = UNSET
    """Percentage of calls made in each state."""

    silent_calls_percentage: Optional[float] = UNSET
    """Percentage of inbound calls with silence tags over total outbound calls. A silent tag is indicative of a
    connectivity issue or muted audio."""


class InsightsV2InboundPhoneNumberReportDict(TypedDict):
    handle: NotRequired[str]
    total_calls: NotRequired[int]
    call_answer_score: NotRequired[float]
    call_state_percentage: NotRequired[CallStatePercentage | CallStatePercentageDict]
    silent_calls_percentage: NotRequired[float]
