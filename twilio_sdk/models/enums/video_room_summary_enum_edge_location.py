from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumEdgeLocation(str, Enum):
    ASHBURN = "ashburn"
    DUBLIN = "dublin"
    FRANKFURT = "frankfurt"
    SINGAPORE = "singapore"
    SYDNEY = "sydney"
    SAO_PAULO = "sao_paulo"
    ROAMING = "roaming"
    UMATILLA = "umatilla"
    TOKYO = "tokyo"

    __str__ = str.__str__


VideoRoomSummaryEnumEdgeLocationOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumEdgeLocation | str, open_enum_validator(VideoRoomSummaryEnumEdgeLocation)
]
