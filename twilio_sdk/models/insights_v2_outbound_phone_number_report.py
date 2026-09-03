from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .answering_machine_detection1 import AnsweringMachineDetection1, AnsweringMachineDetection1Dict
from .call_state_percentage1 import CallStatePercentage1, CallStatePercentage1Dict
from .county_carrier_value import CountyCarrierValue, CountyCarrierValueDict


class InsightsV2OutboundPhoneNumberReport(SdkBaseModel):
    handle: Optional[str] = UNSET
    """The outbound phone number handle."""

    total_calls: Optional[int] = UNSET
    """Total number of outbound calls made with the given handle during the report period."""

    call_answer_score: Optional[float] = UNSET
    """The call answer score measures customers behavior to the delivered calls. The score is a value between 0 and 100,
    where 100 indicates that all calls were successfully answered."""

    calls_by_device_type: Optional[dict[str, int]] = UNSET
    """Number of calls made with each device type. ``voip``, ``mobile``, ``landline``, ``unknown``"""

    answer_rate_device_type: Optional[dict[str, float]] = UNSET
    """Answer rate for each device type. ``voip``, ``mobile``, ``landline``, ``unknown``"""

    call_state_percentage: Optional[CallStatePercentage1] = UNSET
    """Percentage of calls made in each state."""

    blocked_calls_by_carrier: Optional[list[CountyCarrierValue]] = UNSET
    """Percentage of blocked calls by carrier per country."""

    silent_calls_percentage: Optional[float] = UNSET
    """Percentage of calls with silence tags over total calls. A silent tag is indicative of a connectivity issue or
    muted audio."""

    short_duration_calls_percentage: Optional[float] = UNSET
    """Percentage of completed outbound calls under 10 seconds (PSTN Short call tags); More than 15% is typically low
    trust measured."""

    long_duration_calls_percentage: Optional[float] = UNSET
    """Percentage of long duration calls ( >= 60 seconds)"""

    potential_robocalls_percentage: Optional[float] = UNSET
    """Percentage of completed outbound calls to unassigned or unallocated phone numbers."""

    answering_machine_detection: Optional[AnsweringMachineDetection1] = UNSET
    """Number of calls made in answering machine detection (AMD) enabled."""


class InsightsV2OutboundPhoneNumberReportDict(TypedDict):
    handle: NotRequired[str]
    total_calls: NotRequired[int]
    call_answer_score: NotRequired[float]
    calls_by_device_type: NotRequired[dict[str, int]]
    answer_rate_device_type: NotRequired[dict[str, float]]
    call_state_percentage: NotRequired[CallStatePercentage1 | CallStatePercentage1Dict]
    blocked_calls_by_carrier: NotRequired[list[CountyCarrierValue | CountyCarrierValueDict]]
    silent_calls_percentage: NotRequired[float]
    short_duration_calls_percentage: NotRequired[float]
    long_duration_calls_percentage: NotRequired[float]
    potential_robocalls_percentage: NotRequired[float]
    answering_machine_detection: NotRequired[AnsweringMachineDetection1 | AnsweringMachineDetection1Dict]
