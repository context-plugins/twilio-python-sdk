from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .message_type_config import MessageTypeConfig, MessageTypeConfigDict


class SupportedMessageTypes(SdkBaseModel):
    message_types: list[MessageTypeConfig]
    """List of supported message types for opt-out configurations"""


class SupportedMessageTypesDict(TypedDict):
    message_types: list[MessageTypeConfig | MessageTypeConfigDict]
