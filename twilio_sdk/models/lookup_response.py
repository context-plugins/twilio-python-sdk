from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .call_forwarding_info import CallForwardingInfo, CallForwardingInfoDict
from .caller_name_info import CallerNameInfo, CallerNameInfoDict
from .enums.validation_error import ValidationErrorOrStr
from .identity_match_info import IdentityMatchInfo, IdentityMatchInfoDict
from .line_status_info import LineStatusInfo, LineStatusInfoDict
from .line_type_intelligence_info import LineTypeIntelligenceInfo, LineTypeIntelligenceInfoDict
from .reassigned_number_info import ReassignedNumberInfo, ReassignedNumberInfoDict
from .sim_swap_info import SimSwapInfo, SimSwapInfoDict
from .sms_pumping_risk_info import SmsPumpingRiskInfo, SmsPumpingRiskInfoDict


class LookupResponse(SdkBaseModel):
    calling_country_code: OptionalNullable[str] = UNSET
    """International dialing prefix of the phone number defined in the E.164 standard."""

    country_code: OptionalNullable[str] = UNSET
    """The phone number's `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    national_format: OptionalNullable[str] = UNSET
    """The phone number in `national format
    <https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers>`__."""

    valid: Optional[bool] = UNSET
    """Boolean which indicates if the phone number is in a valid range that can be freely assigned by a carrier to a
    user."""

    validation_errors: Optional[list[ValidationErrorOrStr]] = UNSET
    """Contains reasons why a phone number is invalid. Possible values: TOO_SHORT, TOO_LONG, INVALID_BUT_POSSIBLE,
    INVALID_COUNTRY_CODE, INVALID_LENGTH, NOT_A_NUMBER."""

    caller_name: Optional[CallerNameInfo] = UNSET
    sim_swap: Optional[SimSwapInfo] = UNSET
    call_forwarding: Optional[CallForwardingInfo] = UNSET
    line_type_intelligence: Optional[LineTypeIntelligenceInfo] = UNSET
    line_status: Optional[LineStatusInfo] = UNSET
    identity_match: Optional[IdentityMatchInfo] = UNSET
    reassigned_number: Optional[ReassignedNumberInfo] = UNSET
    sms_pumping_risk: Optional[SmsPumpingRiskInfo] = UNSET
    phone_number_quality_score: Optional[Any] = UNSET
    """An object that contains information of a mobile phone number quality score. Quality score will return a risk
    score about the phone number."""

    pre_fill: Optional[Any] = UNSET
    """An object that contains pre fill information. pre_fill will return PII information associated with the phone
    number like first name, last name, address line, country code, state and postal code."""

    url: Optional[str] = UNSET
    """The absolute URL of the resource."""


class LookupResponseDict(TypedDict):
    calling_country_code: NotRequired[str | None]
    country_code: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    national_format: NotRequired[str | None]
    valid: NotRequired[bool]
    validation_errors: NotRequired[list[ValidationErrorOrStr]]
    caller_name: NotRequired[CallerNameInfo | CallerNameInfoDict]
    sim_swap: NotRequired[SimSwapInfo | SimSwapInfoDict]
    call_forwarding: NotRequired[CallForwardingInfo | CallForwardingInfoDict]
    line_type_intelligence: NotRequired[LineTypeIntelligenceInfo | LineTypeIntelligenceInfoDict]
    line_status: NotRequired[LineStatusInfo | LineStatusInfoDict]
    identity_match: NotRequired[IdentityMatchInfo | IdentityMatchInfoDict]
    reassigned_number: NotRequired[ReassignedNumberInfo | ReassignedNumberInfoDict]
    sms_pumping_risk: NotRequired[SmsPumpingRiskInfo | SmsPumpingRiskInfoDict]
    phone_number_quality_score: NotRequired[Any]
    pre_fill: NotRequired[Any]
    url: NotRequired[str]
