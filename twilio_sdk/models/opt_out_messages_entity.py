from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OptOutMessagesEntity(SdkBaseModel):
    keyword_type: str = Field(alias="keywordType")
    """Combination of KeywordType and Locale in format: {KeywordType}.{Locale}

    Valid KeywordTypes: STOP, START, HELP Valid Locales: See LocaleEnum for full list

    Examples: STOP.ENGLISH, START.SPANISH, HELP.FRENCH"""

    message_type: str = Field(alias="messageType")
    """Message type (typically country code or region identifier)"""

    message: str
    """The message text content (max 320 characters)"""


class OptOutMessagesEntityDict(TypedDict):
    keyword_type: str
    message_type: str
    message: str
