from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SummaryEnumAnsweredBy(str, Enum):
    UNKNOWN = "unknown"
    MACHINE_START = "machine_start"
    MACHINE_END_BEEP = "machine_end_beep"
    MACHINE_END_SILENCE = "machine_end_silence"
    MACHINE_END_OTHER = "machine_end_other"
    HUMAN = "human"
    FAX = "fax"

    __str__ = str.__str__


SummaryEnumAnsweredByOrStr: TypeAlias = Annotated[
    SummaryEnumAnsweredBy | str, open_enum_validator(SummaryEnumAnsweredBy)
]
