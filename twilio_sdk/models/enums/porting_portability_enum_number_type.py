from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PortingPortabilityEnumNumberType(str, Enum):
    """The type of the requested phone number. One of ``LOCAL``, ``UNKNOWN``, ``MOBILE``, ``TOLL-FREE``."""

    LOCAL = "LOCAL"
    UNKNOWN = "UNKNOWN"
    MOBILE = "MOBILE"
    TOLL_FREE = "TOLL-FREE"

    __str__ = str.__str__


PortingPortabilityEnumNumberTypeOrStr: TypeAlias = Annotated[
    PortingPortabilityEnumNumberType | str, open_enum_validator(PortingPortabilityEnumNumberType)
]
