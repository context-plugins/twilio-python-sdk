from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SummaryEnumCallState(str, Enum):
    RINGING = "ringing"
    COMPLETED = "completed"
    BUSY = "busy"
    FAIL = "fail"
    NOANSWER = "noanswer"
    CANCELED = "canceled"
    ANSWERED = "answered"
    UNDIALED = "undialed"

    __str__ = str.__str__


SummaryEnumCallStateOrStr: TypeAlias = Annotated[SummaryEnumCallState | str, open_enum_validator(SummaryEnumCallState)]
