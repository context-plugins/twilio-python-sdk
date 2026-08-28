from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EligibilityEnumEligibilityStatus(str, Enum):
    INELIGIBLE = "ineligible"
    ELIGIBLE = "eligible"

    __str__ = str.__str__


EligibilityEnumEligibilityStatusOrStr: TypeAlias = Annotated[
    EligibilityEnumEligibilityStatus | str, open_enum_validator(EligibilityEnumEligibilityStatus)
]
