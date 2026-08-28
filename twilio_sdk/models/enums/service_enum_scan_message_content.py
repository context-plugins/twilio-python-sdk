from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceEnumScanMessageContent(str, Enum):
    """Reserved."""

    INHERIT = "inherit"
    ENABLE = "enable"
    DISABLE = "disable"

    __str__ = str.__str__


ServiceEnumScanMessageContentOrStr: TypeAlias = Annotated[
    ServiceEnumScanMessageContent | str, open_enum_validator(ServiceEnumScanMessageContent)
]
