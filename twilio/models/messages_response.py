from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .message_properties import MessageProperties, MessagePropertiesDict


class MessagesResponse(SdkBaseModel):
    account_sid: str
    """The SID of the account that owns this opt-out configuration"""

    opt_out_sid: str
    """The SID of the opt-out configuration"""

    config: list[MessageProperties]
    """List of message configurations for different keyword types"""


class MessagesResponseDict(TypedDict):
    account_sid: str
    opt_out_sid: str
    config: list[MessageProperties | MessagePropertiesDict]
