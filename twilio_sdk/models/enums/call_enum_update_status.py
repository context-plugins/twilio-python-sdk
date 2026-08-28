from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallEnumUpdateStatus(str, Enum):
    CANCELED = "canceled"
    COMPLETED = "completed"

    __str__ = str.__str__


CallEnumUpdateStatusOrStr: TypeAlias = Annotated[CallEnumUpdateStatus | str, open_enum_validator(CallEnumUpdateStatus)]
