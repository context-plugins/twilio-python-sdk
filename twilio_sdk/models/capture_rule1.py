from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CaptureRule1(SdkBaseModel):
    from_: str = Field(alias="from")
    to: str
    metadata: Optional[dict[str, str]] = UNSET


class CaptureRule1Dict(TypedDict):
    from_: str
    to: str
    metadata: NotRequired[dict[str, str]]
