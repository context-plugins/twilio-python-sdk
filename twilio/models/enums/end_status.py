from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EndStatus(str, Enum):
    """End status of the call wrap up event."""

    UNKNOWN = "unknown"
    FAILURE = "failure"
    ENDED = "ended"
    HUNG_UP = "hung_up"

    __str__ = str.__str__


EndStatusOrStr: TypeAlias = Annotated[EndStatus | str, open_enum_validator(EndStatus)]
