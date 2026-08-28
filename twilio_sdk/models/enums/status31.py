from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status31(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CLOSED = "CLOSED"

    __str__ = str.__str__


Status31OrStr: TypeAlias = Annotated[Status31 | str, open_enum_validator(Status31)]
