from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.method21 import Method21OrStr


class StatusCallback1(SdkBaseModel):
    url: str
    method: Optional[Method21OrStr] = UNSET


class StatusCallback1Dict(TypedDict):
    url: str
    method: NotRequired[Method21OrStr]
