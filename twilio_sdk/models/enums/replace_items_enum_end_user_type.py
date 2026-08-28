from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReplaceItemsEnumEndUserType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    __str__ = str.__str__


ReplaceItemsEnumEndUserTypeOrStr: TypeAlias = Annotated[
    ReplaceItemsEnumEndUserType | str, open_enum_validator(ReplaceItemsEnumEndUserType)
]
