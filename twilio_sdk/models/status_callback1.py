from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.method21 import Method21OrStr


class StatusCallback1(SdkBaseModel):
    url: AnyUrl
    method: Optional[Method21OrStr] = UNSET


class StatusCallback1Dict(TypedDict):
    url: AnyUrl
    method: NotRequired[Method21OrStr]
