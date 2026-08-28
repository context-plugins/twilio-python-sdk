from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .message_type_config import MessageTypeConfig, MessageTypeConfigDict


class MessageTypesResponse(SdkBaseModel):
    account_sid: str
    """The SID of the account that owns this opt-out configuration"""

    opt_out_sid: str
    """The SID of the opt-out configuration"""

    message_types: list[MessageTypeConfig]
    """List of message types associated with this opt-out configuration"""


class MessageTypesResponseDict(TypedDict):
    account_sid: str
    opt_out_sid: str
    message_types: list[MessageTypeConfig | MessageTypeConfigDict]
