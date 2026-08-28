from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferEnumTransferType(str, Enum):
    WARM = "warm"
    COLD = "cold"
    EXTERNAL = "external"

    __str__ = str.__str__


TransferEnumTransferTypeOrStr: TypeAlias = Annotated[
    TransferEnumTransferType | str, open_enum_validator(TransferEnumTransferType)
]
