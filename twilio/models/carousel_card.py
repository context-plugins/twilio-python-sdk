from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carousel_action import CarouselAction, CarouselActionDict


class CarouselCard(SdkBaseModel):
    title: Optional[str] = UNSET
    body: str
    media: str
    actions: list[CarouselAction]


class CarouselCardDict(TypedDict):
    title: NotRequired[str]
    body: str
    media: str
    actions: list[CarouselAction | CarouselActionDict]
