from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.lease_type import LeaseTypeOrStr
from .enums.payment_frequency import PaymentFrequencyOrStr
from .enums.request_type import RequestTypeOrStr
from .enums.traffic_type import TrafficTypeOrStr


class Setup1(SdkBaseModel):
    """Setup configuration for the application."""

    request_type: Optional[RequestTypeOrStr] = UNSET
    traffic_type: Optional[TrafficTypeOrStr] = UNSET
    lease_type: Optional[LeaseTypeOrStr] = UNSET
    payment_frequency: Optional[PaymentFrequencyOrStr] = UNSET
    short_code_preference: Optional[str] = UNSET
    mms_enabled: Optional[bool] = UNSET
    free_to_end_user: Optional[bool] = UNSET
    charges_apply: Optional[bool] = UNSET
    current_provider: Optional[str] = UNSET
    migrated_mms_enabled: Optional[bool] = UNSET
    migrated_live_traffic: Optional[bool] = UNSET


class Setup1Dict(TypedDict):
    request_type: NotRequired[RequestTypeOrStr]
    traffic_type: NotRequired[TrafficTypeOrStr]
    lease_type: NotRequired[LeaseTypeOrStr]
    payment_frequency: NotRequired[PaymentFrequencyOrStr]
    short_code_preference: NotRequired[str]
    mms_enabled: NotRequired[bool]
    free_to_end_user: NotRequired[bool]
    charges_apply: NotRequired[bool]
    current_provider: NotRequired[str]
    migrated_mms_enabled: NotRequired[bool]
    migrated_live_traffic: NotRequired[bool]
