from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaskEnumStatus(str, Enum):
    """The current status of the Task's assignment. Can be: ``pending``, ``reserved``, ``assigned``, ``canceled``,
    ``wrapping``, or ``completed``."""

    PENDING = "pending"
    RESERVED = "reserved"
    ASSIGNED = "assigned"
    CANCELED = "canceled"
    COMPLETED = "completed"
    WRAPPING = "wrapping"

    __str__ = str.__str__


TaskEnumStatusOrStr: TypeAlias = Annotated[TaskEnumStatus | str, open_enum_validator(TaskEnumStatus)]
