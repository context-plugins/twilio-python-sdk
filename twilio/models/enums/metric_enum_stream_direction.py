from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MetricEnumStreamDirection(str, Enum):
    UNKNOWN = "unknown"
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    BOTH = "both"

    __str__ = str.__str__


MetricEnumStreamDirectionOrStr: TypeAlias = Annotated[
    MetricEnumStreamDirection | str, open_enum_validator(MetricEnumStreamDirection)
]
