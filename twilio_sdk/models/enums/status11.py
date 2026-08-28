from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status11(str, Enum):
    """Current status of the Action.
    - PENDING: Action accepted, awaiting downstream confirmation
    - COMPLETED: Downstream backend confirmed the action
    - FAILED: Downstream backend reported a failure"""

    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    __str__ = str.__str__


Status11OrStr: TypeAlias = Annotated[Status11 | str, open_enum_validator(Status11)]
