from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MessageTypeConfig(SdkBaseModel):
    key: str
    """The message type key/identifier (typically country codes or special identifiers)"""

    friendly_name: str
    """Human-readable display name for the message type"""


class MessageTypeConfigDict(TypedDict):
    key: str
    friendly_name: str
