from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TrafficType(str, Enum):
    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"
    BOTH = "BOTH"

    __str__ = str.__str__


TrafficTypeOrStr: TypeAlias = Annotated[TrafficType | str, open_enum_validator(TrafficType)]
