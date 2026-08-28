from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StatusTimeouts1(SdkBaseModel):
    inactive: Optional[int] = UNSET
    closed: Optional[int] = UNSET


class StatusTimeouts1Dict(TypedDict):
    inactive: NotRequired[int]
    closed: NotRequired[int]
