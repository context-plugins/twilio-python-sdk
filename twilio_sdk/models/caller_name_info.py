from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallerNameInfo(SdkBaseModel):
    caller_name: Optional[str] = UNSET
    caller_type: Optional[str] = UNSET
    error_code: Optional[int] = UNSET


class CallerNameInfoDict(TypedDict):
    caller_name: NotRequired[str]
    caller_type: NotRequired[str]
    error_code: NotRequired[int]
