from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OptOutKeywordsEntity(SdkBaseModel):
    keyword_type: str = Field(alias="keywordType")
    """Combination of KeywordType and Locale in format: {KeywordType}.{Locale}

    Valid KeywordTypes: STOP, START, HELP Valid Locales: See LocaleEnum for full list

    Examples: STOP.ENGLISH, START.SPANISH, HELP.FRENCH"""

    message_type: str = Field(alias="messageType")
    """The message type identifier (typically country codes or special identifiers)"""

    keyword: str
    """The keyword to add"""


class OptOutKeywordsEntityDict(TypedDict):
    keyword_type: str
    message_type: str
    keyword: str
