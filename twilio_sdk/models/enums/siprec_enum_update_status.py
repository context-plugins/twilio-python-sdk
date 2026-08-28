from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SiprecEnumUpdateStatus(str, Enum):
    STOPPED = "stopped"

    __str__ = str.__str__


SiprecEnumUpdateStatusOrStr: TypeAlias = Annotated[
    SiprecEnumUpdateStatus | str, open_enum_validator(SiprecEnumUpdateStatus)
]
