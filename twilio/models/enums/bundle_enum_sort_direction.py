from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BundleEnumSortDirection(str, Enum):
    """Sort order direction, ascending or descending"""

    ASC = "ASC"
    DESC = "DESC"

    __str__ = str.__str__


BundleEnumSortDirectionOrStr: TypeAlias = Annotated[
    BundleEnumSortDirection | str, open_enum_validator(BundleEnumSortDirection)
]
