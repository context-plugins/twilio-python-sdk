from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type10 import Type10OrStr


class ContentText1(SdkBaseModel):
    type_: Type10OrStr = Field(alias="type")
    text: str


class ContentText1Dict(TypedDict):
    type_: Type10OrStr
    text: str
