from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BundleCopyEnumEndUserType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    __str__ = str.__str__


BundleCopyEnumEndUserTypeOrStr: TypeAlias = Annotated[
    BundleCopyEnumEndUserType | str, open_enum_validator(BundleCopyEnumEndUserType)
]
