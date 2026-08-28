from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SenderIdPurpose(str, Enum):
    """Purpose for using Sender ID"""

    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"

    __str__ = str.__str__


SenderIdPurposeOrStr: TypeAlias = Annotated[SenderIdPurpose | str, open_enum_validator(SenderIdPurpose)]
