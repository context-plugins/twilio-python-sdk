from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .keyword_item import KeywordItem, KeywordItemDict


class KeywordTypeConfig(SdkBaseModel):
    """Configuration for a specific keyword type (STOP, START, HELP, etc.)"""

    keywords: list[KeywordItem]
    """List of keywords associated with this keyword type"""

    message: str
    """The response message sent when any keyword of this type is received"""


class KeywordTypeConfigDict(TypedDict):
    keywords: list[KeywordItem | KeywordItemDict]
    message: str
