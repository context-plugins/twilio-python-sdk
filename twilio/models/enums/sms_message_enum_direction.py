from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMessageEnumDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND_API = "outbound-api"
    OUTBOUND_CALL = "outbound-call"
    OUTBOUND_REPLY = "outbound-reply"

    __str__ = str.__str__


SmsMessageEnumDirectionOrStr: TypeAlias = Annotated[
    SmsMessageEnumDirection | str, open_enum_validator(SmsMessageEnumDirection)
]
