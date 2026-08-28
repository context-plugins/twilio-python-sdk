from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SyncMapItemEnumQueryFromBoundType(str, Enum):
    INCLUSIVE = "inclusive"
    EXCLUSIVE = "exclusive"

    __str__ = str.__str__


SyncMapItemEnumQueryFromBoundTypeOrStr: TypeAlias = Annotated[
    SyncMapItemEnumQueryFromBoundType | str, open_enum_validator(SyncMapItemEnumQueryFromBoundType)
]
