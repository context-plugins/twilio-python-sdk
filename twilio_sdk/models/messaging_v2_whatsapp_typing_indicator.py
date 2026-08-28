from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class MessagingV2WhatsappTypingIndicator(SdkBaseModel):
    """- Payload for typing indicator request, Typing indicator request for WhatsApp channel. Requires a messageId from
        a recent inbound message."""

    channel: Literal["whatsapp"] = "whatsapp"
    """Shared channel identifier"""

    message_id: str = Field(alias="messageId")
    """Message SID that identifies the conversation thread for the typing indicator. Must be a valid Twilio Message SID
    (SM*) or Media SID (MM*) from an existing WhatsApp conversation."""


class MessagingV2WhatsappTypingIndicatorDict(TypedDict):
    channel: NotRequired[Literal["whatsapp"]]
    message_id: str
