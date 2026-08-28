from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BundleEnumEndUserType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    __str__ = str.__str__


BundleEnumEndUserTypeOrStr: TypeAlias = Annotated[
    BundleEnumEndUserType | str, open_enum_validator(BundleEnumEndUserType)
]
