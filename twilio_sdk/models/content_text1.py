from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ContentText1(SdkBaseModel):
    type_: Literal["TEXT"] = Field(default="TEXT", alias="type")
    text: str


class ContentText1Dict(TypedDict):
    type_: NotRequired[Literal["TEXT"]]
    text: str
