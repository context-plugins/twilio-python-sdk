from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_action import CardAction, CardActionDict


class WhatsappCard(SdkBaseModel):
    """whatsapp/card is a structured template which can be used to send a series of related information. It must include
    a body and at least one additional field."""

    body: str
    footer: Optional[str] = UNSET
    media: Optional[list[str]] = UNSET
    header_text: Optional[str] = UNSET
    actions: Optional[list[CardAction]] = UNSET


class WhatsappCardDict(TypedDict):
    body: str
    footer: NotRequired[str]
    media: NotRequired[list[str]]
    header_text: NotRequired[str]
    actions: NotRequired[list[CardAction | CardActionDict]]
