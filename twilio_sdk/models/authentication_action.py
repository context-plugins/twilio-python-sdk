from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AuthenticationAction(SdkBaseModel):
    type_: Literal["COPY_CODE"] = Field(default="COPY_CODE", alias="type")
    copy_code_text: str


class AuthenticationActionDict(TypedDict):
    type_: NotRequired[Literal["COPY_CODE"]]
    copy_code_text: str
