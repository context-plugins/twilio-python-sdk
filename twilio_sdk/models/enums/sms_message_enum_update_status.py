from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMessageEnumUpdateStatus(str, Enum):
    CANCELED = "canceled"

    __str__ = str.__str__


SmsMessageEnumUpdateStatusOrStr: TypeAlias = Annotated[
    SmsMessageEnumUpdateStatus | str, open_enum_validator(SmsMessageEnumUpdateStatus)
]
