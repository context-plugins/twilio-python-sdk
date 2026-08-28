from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SessionEnumStatus(str, Enum):
    """The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or ``unknown``."""

    OPEN = "open"
    IN_PROGRESS = "in-progress"
    CLOSED = "closed"
    FAILED = "failed"
    UNKNOWN = "unknown"

    __str__ = str.__str__


SessionEnumStatusOrStr: TypeAlias = Annotated[SessionEnumStatus | str, open_enum_validator(SessionEnumStatus)]
