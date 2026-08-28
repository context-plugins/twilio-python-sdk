from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DefaultKeyword(SdkBaseModel):
    keyword: Optional[str] = UNSET
    """The opt-out keyword"""

    message_type: Optional[str] = Field(default=UNSET, alias="messageType")
    """The type of message (SMS, etc.)"""

    language: Optional[str] = UNSET
    """Language code for the message"""

    message: Optional[str] = UNSET
    """The default response message sent when this keyword is used"""


class DefaultKeywordDict(TypedDict):
    keyword: NotRequired[str]
    message_type: NotRequired[str]
    language: NotRequired[str]
    message: NotRequired[str]
