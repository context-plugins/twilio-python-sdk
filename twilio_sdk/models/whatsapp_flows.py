from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WhatsappFlows(SdkBaseModel):
    """whatsapp/flows templates allow you to send multiple messages in a set order with text or select options"""

    body: str
    button_text: str
    subtitle: Optional[str] = UNSET
    media_url: Optional[str] = UNSET
    flow_id: str
    flow_token: Optional[str] = UNSET
    flow_first_page_id: Optional[str] = UNSET
    is_flow_first_page_endpoint: Optional[bool] = UNSET


class WhatsappFlowsDict(TypedDict):
    body: str
    button_text: str
    subtitle: NotRequired[str]
    media_url: NotRequired[str]
    flow_id: str
    flow_token: NotRequired[str]
    flow_first_page_id: NotRequired[str]
    is_flow_first_page_endpoint: NotRequired[bool]
