from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .carousel_card import CarouselCard, CarouselCardDict


class TwilioCarousel(SdkBaseModel):
    """twilio/carousel templates allow you to send a single text message accompanied by a set of up to 10 carousel cards
    in a horizontally scrollable view"""

    body: str
    cards: list[CarouselCard]


class TwilioCarouselDict(TypedDict):
    body: str
    cards: list[CarouselCard | CarouselCardDict]
