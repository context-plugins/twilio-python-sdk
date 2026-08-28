from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status4(str, Enum):
    UNKNOWN = "unknown"
    CREATION_IN_PROGRESS = "creation-in-progress"
    READY = "ready"
    CREATION_FAILED = "creation-failed"
    DELETION_IN_PROGRESS = "deletion-in-progress"
    DELETED = "deleted"
    DELETION_FAILED = "deletion-failed"

    __str__ = str.__str__


Status4OrStr: TypeAlias = Annotated[Status4 | str, open_enum_validator(Status4)]
