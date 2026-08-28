from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EventEnumTwilioEdge(str, Enum):
    UNKNOWN_EDGE = "unknown_edge"
    CARRIER_EDGE = "carrier_edge"
    SIP_EDGE = "sip_edge"
    SDK_EDGE = "sdk_edge"
    CLIENT_EDGE = "client_edge"

    __str__ = str.__str__


EventEnumTwilioEdgeOrStr: TypeAlias = Annotated[EventEnumTwilioEdge | str, open_enum_validator(EventEnumTwilioEdge)]
