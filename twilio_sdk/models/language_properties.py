from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.key import KeyOrStr


class LanguageProperties(SdkBaseModel):
    key: KeyOrStr
    """The language key/identifier (typically uppercase)"""

    friendly_name: str
    """Human-readable display name for the language"""


class LanguagePropertiesDict(TypedDict):
    key: KeyOrStr
    friendly_name: str
