from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LeaseType(str, Enum):
    RANDOM = "RANDOM"
    VANITY = "VANITY"
    SELF_LEASED = "SELF_LEASED"

    __str__ = str.__str__


LeaseTypeOrStr: TypeAlias = Annotated[LeaseType | str, open_enum_validator(LeaseType)]
