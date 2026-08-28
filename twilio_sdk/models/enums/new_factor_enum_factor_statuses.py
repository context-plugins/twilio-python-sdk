from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewFactorEnumFactorStatuses(str, Enum):
    """The Status of this Factor. One of ``unverified`` or ``verified``."""

    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    __str__ = str.__str__


NewFactorEnumFactorStatusesOrStr: TypeAlias = Annotated[
    NewFactorEnumFactorStatuses | str, open_enum_validator(NewFactorEnumFactorStatuses)
]
