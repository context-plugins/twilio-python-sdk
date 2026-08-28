from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumVettingProvider(str, Enum):
    """The third-party political vetting provider."""

    CAMPAIGN_VERIFY = "CAMPAIGN_VERIFY"

    __str__ = str.__str__


TollfreeVerificationEnumVettingProviderOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumVettingProvider | str, open_enum_validator(TollfreeVerificationEnumVettingProvider)
]
