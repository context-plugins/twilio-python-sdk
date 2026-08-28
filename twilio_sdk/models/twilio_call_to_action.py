from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .call_to_action_action import CallToActionAction, CallToActionActionDict


class TwilioCallToAction(SdkBaseModel):
    """twilio/call-to-action buttons let recipients tap to trigger actions such as launching a website or making a phone
    call."""

    body: str
    actions: list[CallToActionAction]


class TwilioCallToActionDict(TypedDict):
    body: str
    actions: list[CallToActionAction | CallToActionActionDict]
