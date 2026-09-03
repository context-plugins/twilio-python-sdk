from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumBusinessType(str, Enum):
    """The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, SOLE_PROPRIETOR, GOVERNMENT.
    Required field., Type of Business."""

    PRIVATE_PROFIT = "PRIVATE_PROFIT"
    PUBLIC_PROFIT = "PUBLIC_PROFIT"
    SOLE_PROPRIETOR = "SOLE_PROPRIETOR"
    NON_PROFIT = "NON_PROFIT"
    GOVERNMENT = "GOVERNMENT"

    __str__ = str.__str__


TollfreeVerificationEnumBusinessTypeOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumBusinessType | str, open_enum_validator(TollfreeVerificationEnumBusinessType)
]
