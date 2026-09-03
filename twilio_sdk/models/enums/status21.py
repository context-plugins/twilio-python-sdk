from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status21(str, Enum):
    """Current status of the operation."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    __str__ = str.__str__


Status21OrStr: TypeAlias = Annotated[Status21 | str, open_enum_validator(Status21)]
