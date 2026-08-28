from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Event(str, Enum):
    """The type of typing event. "START" indicates the agent began typing, "END" indicates the agent stopped typing.
    Defaults to "START"."""

    START = "START"
    END = "END"

    __str__ = str.__str__


EventOrStr: TypeAlias = Annotated[Event | str, open_enum_validator(Event)]
