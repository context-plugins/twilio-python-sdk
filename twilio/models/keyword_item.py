from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class KeywordItem(SdkBaseModel):
    """Individual keyword configuration"""

    keyword: str
    """The actual keyword text"""

    reserved: bool
    """Indicates whether this keyword is reserved by the system and cannot be modified"""


class KeywordItemDict(TypedDict):
    keyword: str
    reserved: bool
