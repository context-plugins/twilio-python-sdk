from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .keyword_configuration import KeywordConfiguration, KeywordConfigurationDict


class KeywordsResponse(SdkBaseModel):
    account_sid: str
    """The SID of the account that owns this opt-out configuration"""

    opt_out_sid: str
    """The SID of the opt-out configuration"""

    config: list[KeywordConfiguration]
    """List of keyword configurations for different keyword types"""


class KeywordsResponseDict(TypedDict):
    account_sid: str
    opt_out_sid: str
    config: list[KeywordConfiguration | KeywordConfigurationDict]
