from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExecutionEnumStatus(str, Enum):
    """The status of the Execution. Can be: ``active`` or ``ended``."""

    ACTIVE = "active"
    ENDED = "ended"

    __str__ = str.__str__


ExecutionEnumStatusOrStr: TypeAlias = Annotated[ExecutionEnumStatus | str, open_enum_validator(ExecutionEnumStatus)]
