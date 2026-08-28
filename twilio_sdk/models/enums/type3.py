from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type3(str, Enum):
    HUMAN_AGENT = "HUMAN_AGENT"
    CUSTOMER = "CUSTOMER"
    AI_AGENT = "AI_AGENT"
    AGENT = "AGENT"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


Type3OrStr: TypeAlias = Annotated[Type3 | str, open_enum_validator(Type3)]
