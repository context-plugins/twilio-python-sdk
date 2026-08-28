from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionTransferEnumTransferType(str, Enum):
    """The type of the Transfer. Can be: ``cold``, ``warm``."""

    WARM = "warm"
    COLD = "cold"
    EXTERNAL = "external"

    __str__ = str.__str__


InteractionTransferEnumTransferTypeOrStr: TypeAlias = Annotated[
    InteractionTransferEnumTransferType | str, open_enum_validator(InteractionTransferEnumTransferType)
]
