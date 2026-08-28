from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BrandVettingEnumVettingProvider(str, Enum):
    """The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign Verify tokens) or
    “AEGIS” (Secondary Vetting)."""

    CAMPAIGN_VERIFY = "campaign-verify"
    AEGIS = "aegis"

    __str__ = str.__str__


BrandVettingEnumVettingProviderOrStr: TypeAlias = Annotated[
    BrandVettingEnumVettingProvider | str, open_enum_validator(BrandVettingEnumVettingProvider)
]
