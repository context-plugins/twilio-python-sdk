from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorEvent(SdkBaseModel):
    error_code: Optional[int] = UNSET
    """Error code."""

    message: Optional[str] = UNSET
    """Error message."""


class ErrorEventDict(TypedDict):
    error_code: NotRequired[int]
    message: NotRequired[str]
