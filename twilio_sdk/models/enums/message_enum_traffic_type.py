from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumTrafficType(str, Enum):
    FREE = "free"

    __str__ = str.__str__


MessageEnumTrafficTypeOrStr: TypeAlias = Annotated[
    MessageEnumTrafficType | str, open_enum_validator(MessageEnumTrafficType)
]
