from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field_model import FieldModelOrStr
from .identity_match_parameters import IdentityMatchParameters, IdentityMatchParametersDict
from .reassigned_number_parameters import ReassignedNumberParameters, ReassignedNumberParametersDict
from .risk_parameters import RiskParameters, RiskParametersDict


class LookupRequestWithCorId(SdkBaseModel):
    correlation_id: Optional[str] = UNSET
    """Unique identifier used to match request with response"""

    phone_number: str
    fields: Optional[list[FieldModelOrStr]] = UNSET
    country_code: Optional[str] = UNSET
    identity_match: Optional[IdentityMatchParameters] = UNSET
    reassigned_number: Optional[ReassignedNumberParameters] = UNSET
    sms_pumping_risk: Optional[RiskParameters] = UNSET


class LookupRequestWithCorIdDict(TypedDict):
    correlation_id: NotRequired[str]
    phone_number: str
    fields: NotRequired[list[FieldModelOrStr]]
    country_code: NotRequired[str]
    identity_match: NotRequired[IdentityMatchParameters | IdentityMatchParametersDict]
    reassigned_number: NotRequired[ReassignedNumberParameters | ReassignedNumberParametersDict]
    sms_pumping_risk: NotRequired[RiskParameters | RiskParametersDict]
