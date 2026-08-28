from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.quick_reply_action_type import QuickReplyActionTypeOrStr


class QuickReplyAction(SdkBaseModel):
    type_: Optional[QuickReplyActionTypeOrStr] = Field(default=UNSET, alias="type")
    title: str
    id: Optional[str] = UNSET


class QuickReplyActionDict(TypedDict):
    type_: NotRequired[QuickReplyActionTypeOrStr]
    title: str
    id: NotRequired[str]
