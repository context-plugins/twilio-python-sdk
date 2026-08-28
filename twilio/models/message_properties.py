from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MessageProperties(SdkBaseModel):
    keyword_type: str
    """The keyword type in format KeywordType.Locale (e.g., STOP.ENGLISH, HELP.FRENCH)"""

    message_type: str
    """The message type identifier (typically country codes or special identifiers)"""

    message: str
    """The actual opt-out message text to be sent"""


class MessagePropertiesDict(TypedDict):
    keyword_type: str
    message_type: str
    message: str
