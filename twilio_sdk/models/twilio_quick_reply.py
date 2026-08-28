from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .quick_reply_action import QuickReplyAction, QuickReplyActionDict


class TwilioQuickReply(SdkBaseModel):
    """twilio/quick-reply templates let recipients tap, rather than type, to respond to the message."""

    body: str
    actions: list[QuickReplyAction]


class TwilioQuickReplyDict(TypedDict):
    body: str
    actions: list[QuickReplyAction | QuickReplyActionDict]
