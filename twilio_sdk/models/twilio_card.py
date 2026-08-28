from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_action import CardAction, CardActionDict


class TwilioCard(SdkBaseModel):
    """twilio/card is a structured template which can be used to send a series of related information. It must include a
    title and at least one additional field."""

    title: Optional[str] = UNSET
    subtitle: Optional[str] = UNSET
    media: Optional[list[str]] = UNSET
    actions: Optional[list[CardAction]] = UNSET


class TwilioCardDict(TypedDict):
    title: NotRequired[str]
    subtitle: NotRequired[str]
    media: NotRequired[list[str]]
    actions: NotRequired[list[CardAction | CardActionDict]]
