from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaskReservationEnumSupervisorMode(str, Enum):
    MONITOR = "monitor"
    WHISPER = "whisper"
    BARGE = "barge"

    __str__ = str.__str__


TaskReservationEnumSupervisorModeOrStr: TypeAlias = Annotated[
    TaskReservationEnumSupervisorMode | str, open_enum_validator(TaskReservationEnumSupervisorMode)
]
