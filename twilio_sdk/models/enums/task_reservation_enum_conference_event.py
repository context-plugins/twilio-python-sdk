from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaskReservationEnumConferenceEvent(str, Enum):
    START = "start"
    END = "end"
    JOIN = "join"
    LEAVE = "leave"
    MUTE = "mute"
    HOLD = "hold"
    SPEAKER = "speaker"

    __str__ = str.__str__


TaskReservationEnumConferenceEventOrStr: TypeAlias = Annotated[
    TaskReservationEnumConferenceEvent | str, open_enum_validator(TaskReservationEnumConferenceEvent)
]
