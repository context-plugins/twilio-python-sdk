from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SummaryEnumCallType(str, Enum):
    CARRIER = "carrier"
    SIP = "sip"
    TRUNKING = "trunking"
    CLIENT = "client"
    WHATSAPP = "whatsapp"

    __str__ = str.__str__


SummaryEnumCallTypeOrStr: TypeAlias = Annotated[SummaryEnumCallType | str, open_enum_validator(SummaryEnumCallType)]
