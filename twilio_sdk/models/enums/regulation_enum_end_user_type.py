from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RegulationEnumEndUserType(str, Enum):
    """The type of End User the regulation requires - can be ``individual`` or ``business``."""

    INDIVIDUAL = "individual"
    BUSINESS = "business"

    __str__ = str.__str__


RegulationEnumEndUserTypeOrStr: TypeAlias = Annotated[
    RegulationEnumEndUserType | str, open_enum_validator(RegulationEnumEndUserType)
]
