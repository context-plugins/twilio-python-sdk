from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BundleEnumSortBy(str, Enum):
    VALID_UNTIL = "valid-until"
    DATE_UPDATED = "date-updated"

    __str__ = str.__str__


BundleEnumSortByOrStr: TypeAlias = Annotated[BundleEnumSortBy | str, open_enum_validator(BundleEnumSortBy)]
