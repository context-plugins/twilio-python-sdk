from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BulkEligibilityEnumEligibilityStatus(str, Enum):
    INELIGIBLE = "ineligible"
    ELIGIBLE = "eligible"

    __str__ = str.__str__


BulkEligibilityEnumEligibilityStatusOrStr: TypeAlias = Annotated[
    BulkEligibilityEnumEligibilityStatus | str, open_enum_validator(BulkEligibilityEnumEligibilityStatus)
]
