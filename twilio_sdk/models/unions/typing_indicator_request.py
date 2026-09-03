from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..apple_typing_indicator_request import AppleTypingIndicatorRequest, AppleTypingIndicatorRequestDict
from ..messaging_v2_whatsapp_typing_indicator import (
    MessagingV2WhatsappTypingIndicator,
    MessagingV2WhatsappTypingIndicatorDict,
)

TypingIndicatorRequest: TypeAlias = Annotated[
    MessagingV2WhatsappTypingIndicator | AppleTypingIndicatorRequest, Field(discriminator="channel")
]
"""Request body for sending a typing indicator. The schema varies by channel. Use the ``channel`` field to determine
which properties are required."""

TypingIndicatorRequestDict: TypeAlias = MessagingV2WhatsappTypingIndicatorDict | AppleTypingIndicatorRequestDict
