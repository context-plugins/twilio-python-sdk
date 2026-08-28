from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IdentityMatchInfo(SdkBaseModel):
    first_name_match: Optional[str] = UNSET
    last_name_match: Optional[str] = UNSET
    address_lines_match: Optional[str] = UNSET
    city_match: Optional[str] = UNSET
    state_match: Optional[str] = UNSET
    postal_code_match: Optional[str] = UNSET
    address_country_match: Optional[str] = UNSET
    national_id_match: Optional[str] = UNSET
    date_of_birth_match: Optional[str] = UNSET
    summary_score: Optional[int] = UNSET
    error_code: Optional[int] = UNSET
    error_message: Optional[str] = UNSET


class IdentityMatchInfoDict(TypedDict):
    first_name_match: NotRequired[str]
    last_name_match: NotRequired[str]
    address_lines_match: NotRequired[str]
    city_match: NotRequired[str]
    state_match: NotRequired[str]
    postal_code_match: NotRequired[str]
    address_country_match: NotRequired[str]
    national_id_match: NotRequired[str]
    date_of_birth_match: NotRequired[str]
    summary_score: NotRequired[int]
    error_code: NotRequired[int]
    error_message: NotRequired[str]
