from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReassignedNumberInfo(SdkBaseModel):
    last_verified_date: Optional[str] = UNSET
    is_number_reassigned: Optional[str] = UNSET
    error_code: Optional[str] = UNSET


class ReassignedNumberInfoDict(TypedDict):
    last_verified_date: NotRequired[str]
    is_number_reassigned: NotRequired[str]
    error_code: NotRequired[str]
