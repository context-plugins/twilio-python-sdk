from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamEnumUpdateStatus(str, Enum):
    STOPPED = "stopped"

    __str__ = str.__str__


StreamEnumUpdateStatusOrStr: TypeAlias = Annotated[
    StreamEnumUpdateStatus | str, open_enum_validator(StreamEnumUpdateStatus)
]
