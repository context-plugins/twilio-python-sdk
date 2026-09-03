from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type4 import Type4OrStr


class InterruptEvent(SdkBaseModel):
    type_: Optional[Type4OrStr] = Field(default=UNSET, alias="type")
    """Type of interruption event."""


class InterruptEventDict(TypedDict):
    type_: NotRequired[Type4OrStr]
