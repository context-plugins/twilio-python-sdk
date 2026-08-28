from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.op import OpOrStr
from .expression import Expression, ExpressionDict


class Filter(SdkBaseModel):
    op: Optional[OpOrStr] = UNSET
    expressions: list[Expression]


class FilterDict(TypedDict):
    op: NotRequired[OpOrStr]
    expressions: list[Expression | ExpressionDict]
