from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type11 import Type11OrStr


class ContentText(SdkBaseModel):
    type_: Type11OrStr = Field(alias="type")
    """Content type discriminator."""

    text: str
    """Message text content."""


class ContentTextDict(TypedDict):
    type_: Type11OrStr
    text: str
