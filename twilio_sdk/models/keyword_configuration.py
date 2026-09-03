from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class KeywordConfiguration(SdkBaseModel):
    keyword_type: str
    """The keyword type in format KeywordType.Locale (e.g., STOP.ENGLISH, HELP.FRENCH)"""

    message_type: str
    """The message type identifier (typically country codes or special identifiers)"""

    keywords: list[str]
    """Array of keyword strings for this configuration"""


class KeywordConfigurationDict(TypedDict):
    keyword_type: str
    message_type: str
    keywords: list[str]
