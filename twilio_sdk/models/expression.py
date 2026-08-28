from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.op import OpOrStr


class Expression(SdkBaseModel):
    op: OpOrStr
    field: str
    values: Optional[list[str]] = UNSET


class ExpressionDict(TypedDict):
    op: OpOrStr
    field: str
    values: NotRequired[list[str]]
