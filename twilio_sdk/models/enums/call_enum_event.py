from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallEnumEvent(str, Enum):
    INITIATED = "initiated"
    RINGING = "ringing"
    ANSWERED = "answered"
    COMPLETED = "completed"

    __str__ = str.__str__


CallEnumEventOrStr: TypeAlias = Annotated[CallEnumEvent | str, open_enum_validator(CallEnumEvent)]
