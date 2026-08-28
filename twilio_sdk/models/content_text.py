from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ContentText(SdkBaseModel):
    type_: Literal["TEXT"] = Field(default="TEXT", alias="type")
    """Content type discriminator."""

    text: str
    """Message text content."""


class ContentTextDict(TypedDict):
    type_: NotRequired[Literal["TEXT"]]
    text: str
