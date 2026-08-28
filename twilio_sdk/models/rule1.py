from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Rule1(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    all: Optional[bool] = UNSET
    publisher: Optional[str] = UNSET
    track: Optional[str] = UNSET
    kind: Optional[str] = UNSET


class Rule1Dict(TypedDict):
    type_: NotRequired[str]
    all: NotRequired[bool]
    publisher: NotRequired[str]
    track: NotRequired[str]
    kind: NotRequired[str]
