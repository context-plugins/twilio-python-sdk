from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LineStatusInfo(SdkBaseModel):
    status: Optional[str] = UNSET
    error_code: Optional[int] = UNSET


class LineStatusInfoDict(TypedDict):
    status: NotRequired[str]
    error_code: NotRequired[int]
