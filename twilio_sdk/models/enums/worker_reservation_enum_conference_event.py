from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkerReservationEnumConferenceEvent(str, Enum):
    START = "start"
    END = "end"
    JOIN = "join"
    LEAVE = "leave"
    MUTE = "mute"
    HOLD = "hold"
    SPEAKER = "speaker"

    __str__ = str.__str__


WorkerReservationEnumConferenceEventOrStr: TypeAlias = Annotated[
    WorkerReservationEnumConferenceEvent | str, open_enum_validator(WorkerReservationEnumConferenceEvent)
]
