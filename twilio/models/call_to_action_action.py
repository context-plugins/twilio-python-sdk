from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.call_to_action_action_type import CallToActionActionTypeOrStr


class CallToActionAction(SdkBaseModel):
    type_: CallToActionActionTypeOrStr = Field(alias="type")
    title: str
    url: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    code: Optional[str] = UNSET
    id: Optional[str] = UNSET


class CallToActionActionDict(TypedDict):
    type_: CallToActionActionTypeOrStr
    title: str
    url: NotRequired[str]
    phone: NotRequired[str]
    code: NotRequired[str]
    id: NotRequired[str]
