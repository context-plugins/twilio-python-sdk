from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SummaryEnumProcessingState(str, Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"

    __str__ = str.__str__


SummaryEnumProcessingStateOrStr: TypeAlias = Annotated[
    SummaryEnumProcessingState | str, open_enum_validator(SummaryEnumProcessingState)
]
