from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EventEnumLevel(str, Enum):
    UNKNOWN = "UNKNOWN"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

    __str__ = str.__str__


EventEnumLevelOrStr: TypeAlias = Annotated[EventEnumLevel | str, open_enum_validator(EventEnumLevel)]
