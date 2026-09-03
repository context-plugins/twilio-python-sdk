from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamEnumStatus(str, Enum):
    """The status of the Stream. Possible values are ``stopped`` and ``in-progress``."""

    IN_PROGRESS = "in-progress"
    STOPPED = "stopped"

    __str__ = str.__str__


StreamEnumStatusOrStr: TypeAlias = Annotated[StreamEnumStatus | str, open_enum_validator(StreamEnumStatus)]
