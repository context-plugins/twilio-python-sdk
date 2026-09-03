from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumCallType(str, Enum):
    CARRIER = "carrier"
    SIP = "sip"
    TRUNKING = "trunking"
    CLIENT = "client"
    WHATSAPP = "whatsapp"

    __str__ = str.__str__


CallSummariesEnumCallTypeOrStr: TypeAlias = Annotated[
    CallSummariesEnumCallType | str, open_enum_validator(CallSummariesEnumCallType)
]
