from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .answering_machine_detection import AnsweringMachineDetection, AnsweringMachineDetectionDict
from .call_direction import CallDirection, CallDirectionDict
from .call_state import CallState, CallStateDict
from .call_type import CallType, CallTypeDict
from .kyt import Kyt, KytDict
from .network_issues import NetworkIssues, NetworkIssuesDict


class AccountReport(SdkBaseModel):
    call_deliverability_score: Optional[float] = UNSET
    """The call deliverability score measures the network effectiveness in delivering calls by scoring calls reach the
    intended recipient. The score is a value between 0 and 100, where 100 indicates that all calls were successfully
    delivered."""

    call_answer_score: Optional[float] = UNSET
    """The call answer score measures customers behavior to the delivered calls. The score is a value between 0 and 100,
    where 100 indicates that all calls were successfully answered."""

    total_calls: Optional[int] = UNSET
    """Total number of calls made during the report period."""

    call_direction: Optional[CallDirection] = UNSET
    """Number of calls made in each direction."""

    call_state: Optional[CallState] = UNSET
    """Number of calls made in each state."""

    call_type: Optional[CallType] = UNSET
    """Number of calls made in each type. ``carrier``, ``sip``, ``trunking``, ``client``, ``whatsapp``"""

    aloc: Optional[float] = UNSET
    """Average length of call in seconds."""

    twilio_edge_location: Optional[dict[str, int]] = UNSET
    """Number of calls made in each Twilio Edge location. Refer to `Public Edge Locations
    <https://www.twilio.com/docs/global-infrastructure/edge-locations#public-edge-locations>`__ for more detail."""

    caller_country_code: Optional[dict[str, int]] = UNSET
    """Number of calls originating from each country (ISO alpha-2)."""

    callee_country_code: Optional[dict[str, int]] = UNSET
    """Number of calls terminating in each country (ISO alpha-2)."""

    average_queue_time_ms: Optional[float] = UNSET
    """Average queue time in milliseconds."""

    silent_calls_percentage: Optional[float] = UNSET
    """Percentage of silent calls."""

    network_issues: Optional[NetworkIssues] = UNSET
    """Network-quality indicators for SDK and Twilio Gateway traffic during the report period."""

    kyt: Optional[Kyt] = Field(default=UNSET, alias="KYT")
    """Know Your Traffic (KYT) metrics focused on outbound carrier performance and trust signals for the report
    period."""

    answering_machine_detection: Optional[AnsweringMachineDetection] = UNSET
    """Number of calls made in each answering machine detection."""


class AccountReportDict(TypedDict):
    call_deliverability_score: NotRequired[float]
    call_answer_score: NotRequired[float]
    total_calls: NotRequired[int]
    call_direction: NotRequired[CallDirection | CallDirectionDict]
    call_state: NotRequired[CallState | CallStateDict]
    call_type: NotRequired[CallType | CallTypeDict]
    aloc: NotRequired[float]
    twilio_edge_location: NotRequired[dict[str, int]]
    caller_country_code: NotRequired[dict[str, int]]
    callee_country_code: NotRequired[dict[str, int]]
    average_queue_time_ms: NotRequired[float]
    silent_calls_percentage: NotRequired[float]
    network_issues: NotRequired[NetworkIssues | NetworkIssuesDict]
    kyt: NotRequired[Kyt | KytDict]
    answering_machine_detection: NotRequired[AnsweringMachineDetection | AnsweringMachineDetectionDict]
