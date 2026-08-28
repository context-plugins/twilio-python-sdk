from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferEnumTransferStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    COMPLETED = "completed"

    __str__ = str.__str__


TransferEnumTransferStatusOrStr: TypeAlias = Annotated[
    TransferEnumTransferStatus | str, open_enum_validator(TransferEnumTransferStatus)
]
