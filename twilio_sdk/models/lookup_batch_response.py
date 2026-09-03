from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .call_forwarding_info import CallForwardingInfo, CallForwardingInfoDict
from .caller_name_info import CallerNameInfo, CallerNameInfoDict
from .identity_match_info import IdentityMatchInfo, IdentityMatchInfoDict
from .line_status_info import LineStatusInfo, LineStatusInfoDict
from .line_type_intelligence_info import LineTypeIntelligenceInfo, LineTypeIntelligenceInfoDict
from .reassigned_number_info import ReassignedNumberInfo, ReassignedNumberInfoDict
from .sim_swap_info import SimSwapInfo, SimSwapInfoDict
from .sms_pumping_risk_info import SmsPumpingRiskInfo, SmsPumpingRiskInfoDict


class LookupBatchResponse(SdkBaseModel):
    correlation_id: Optional[str] = UNSET
    """Unique identifier used to match request with response"""

    twilio_error_code: Optional[int] = UNSET
    """Twilio error code in case that the request to downstream fails"""

    calling_country_code: Optional[str] = UNSET
    country_code: Optional[str] = UNSET
    phone_number: Optional[str] = UNSET
    national_format: Optional[str] = UNSET
    valid: Optional[bool] = UNSET
    validation_errors: Optional[list[str]] = UNSET
    caller_name: Optional[CallerNameInfo] = UNSET
    sim_swap: Optional[SimSwapInfo] = UNSET
    call_forwarding: Optional[CallForwardingInfo] = UNSET
    line_type_intelligence: Optional[LineTypeIntelligenceInfo] = UNSET
    line_status: Optional[LineStatusInfo] = UNSET
    identity_match: Optional[IdentityMatchInfo] = UNSET
    reassigned_number: Optional[ReassignedNumberInfo] = UNSET
    sms_pumping_risk: Optional[SmsPumpingRiskInfo] = UNSET
    phone_number_quality_score: OptionalNullable[Any] = UNSET
    pre_fill: OptionalNullable[Any] = UNSET


class LookupBatchResponseDict(TypedDict):
    correlation_id: NotRequired[str]
    twilio_error_code: NotRequired[int]
    calling_country_code: NotRequired[str]
    country_code: NotRequired[str]
    phone_number: NotRequired[str]
    national_format: NotRequired[str]
    valid: NotRequired[bool]
    validation_errors: NotRequired[list[str]]
    caller_name: NotRequired[CallerNameInfo | CallerNameInfoDict]
    sim_swap: NotRequired[SimSwapInfo | SimSwapInfoDict]
    call_forwarding: NotRequired[CallForwardingInfo | CallForwardingInfoDict]
    line_type_intelligence: NotRequired[LineTypeIntelligenceInfo | LineTypeIntelligenceInfoDict]
    line_status: NotRequired[LineStatusInfo | LineStatusInfoDict]
    identity_match: NotRequired[IdentityMatchInfo | IdentityMatchInfoDict]
    reassigned_number: NotRequired[ReassignedNumberInfo | ReassignedNumberInfoDict]
    sms_pumping_risk: NotRequired[SmsPumpingRiskInfo | SmsPumpingRiskInfoDict]
    phone_number_quality_score: NotRequired[Any | None]
    pre_fill: NotRequired[Any | None]
