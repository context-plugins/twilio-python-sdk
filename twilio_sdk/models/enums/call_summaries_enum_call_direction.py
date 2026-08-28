from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumCallDirection(str, Enum):
    OUTBOUND_API = "outbound_api"
    OUTBOUND_DIAL = "outbound_dial"
    INBOUND = "inbound"
    TRUNKING_ORIGINATING = "trunking_originating"
    TRUNKING_TERMINATING = "trunking_terminating"

    __str__ = str.__str__


CallSummariesEnumCallDirectionOrStr: TypeAlias = Annotated[
    CallSummariesEnumCallDirection | str, open_enum_validator(CallSummariesEnumCallDirection)
]
