from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.carousel_action_type import CarouselActionTypeOrStr


class CarouselAction(SdkBaseModel):
    type_: CarouselActionTypeOrStr = Field(alias="type")
    title: str
    url: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    id: Optional[str] = UNSET


class CarouselActionDict(TypedDict):
    type_: CarouselActionTypeOrStr
    title: str
    url: NotRequired[str]
    phone: NotRequired[str]
    id: NotRequired[str]
