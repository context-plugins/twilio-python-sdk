from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.card_action_type import CardActionTypeOrStr
from .enums.webview_size_type import WebviewSizeTypeOrStr


class CardAction(SdkBaseModel):
    type_: CardActionTypeOrStr = Field(alias="type")
    title: str
    url: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    id: Optional[str] = UNSET
    code: Optional[str] = UNSET
    webview_size: Optional[WebviewSizeTypeOrStr] = UNSET


class CardActionDict(TypedDict):
    type_: CardActionTypeOrStr
    title: str
    url: NotRequired[str]
    phone: NotRequired[str]
    id: NotRequired[str]
    code: NotRequired[str]
    webview_size: NotRequired[WebviewSizeTypeOrStr]
