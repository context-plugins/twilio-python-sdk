from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumSortBy(str, Enum):
    START_TIME = "start_time"
    END_TIME = "end_time"

    __str__ = str.__str__


CallSummariesEnumSortByOrStr: TypeAlias = Annotated[
    CallSummariesEnumSortBy | str, open_enum_validator(CallSummariesEnumSortBy)
]
