from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumProcessingState(str, Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"

    __str__ = str.__str__


CallSummariesEnumProcessingStateOrStr: TypeAlias = Annotated[
    CallSummariesEnumProcessingState | str, open_enum_validator(CallSummariesEnumProcessingState)
]
