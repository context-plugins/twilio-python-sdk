from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionTransferEnumTransferStatus(str, Enum):
    """The status of the Transfer. Can be: ``active``, ``completed``, ``failed``."""

    ACTIVE = "active"
    FAILED = "failed"
    COMPLETED = "completed"

    __str__ = str.__str__


InteractionTransferEnumTransferStatusOrStr: TypeAlias = Annotated[
    InteractionTransferEnumTransferStatus | str, open_enum_validator(InteractionTransferEnumTransferStatus)
]
