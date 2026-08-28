from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EndUserEnumType(str, Enum):
    """The type of end user of the Bundle resource - can be ``individual`` or ``business``."""

    INDIVIDUAL = "individual"
    BUSINESS = "business"

    __str__ = str.__str__


EndUserEnumTypeOrStr: TypeAlias = Annotated[EndUserEnumType | str, open_enum_validator(EndUserEnumType)]
