from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumUpdateStatus(str, Enum):
    CANCELED = "canceled"

    __str__ = str.__str__


MessageEnumUpdateStatusOrStr: TypeAlias = Annotated[
    MessageEnumUpdateStatus | str, open_enum_validator(MessageEnumUpdateStatus)
]
