from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flows_page import FlowsPage, FlowsPageDict


class TwilioFlows(SdkBaseModel):
    """twilio/flows templates allow you to send multiple messages in a set order with text or select options"""

    body: str
    button_text: str
    subtitle: Optional[str] = UNSET
    media_url: Optional[str] = UNSET
    pages: list[FlowsPage]
    type_: str = Field(alias="type")


class TwilioFlowsDict(TypedDict):
    body: str
    button_text: str
    subtitle: NotRequired[str]
    media_url: NotRequired[str]
    pages: list[FlowsPage | FlowsPageDict]
    type_: str
