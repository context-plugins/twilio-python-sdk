from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class SmsPumpingRiskInfo(SdkBaseModel):
    carrier_risk_category: Optional[str] = UNSET
    number_blocked: Optional[bool] = UNSET
    number_blocked_date: Optional[RFC3339DateTime] = UNSET
    number_blocked_last_3_months: Optional[bool] = UNSET
    sms_pumping_risk_score: Optional[int] = UNSET
    error_code: Optional[int] = UNSET


class SmsPumpingRiskInfoDict(TypedDict):
    carrier_risk_category: NotRequired[str]
    number_blocked: NotRequired[bool]
    number_blocked_date: NotRequired[RFC3339DateTime]
    number_blocked_last_3_months: NotRequired[bool]
    sms_pumping_risk_score: NotRequired[int]
    error_code: NotRequired[int]
