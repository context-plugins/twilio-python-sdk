from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type111(str, Enum):
    TRANSCRIPTION = "TRANSCRIPTION"

    __str__ = str.__str__


Type111OrStr: TypeAlias = Annotated[Type111 | str, open_enum_validator(Type111)]
