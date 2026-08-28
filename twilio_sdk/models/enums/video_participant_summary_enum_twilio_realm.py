from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoParticipantSummaryEnumTwilioRealm(str, Enum):
    US1 = "us1"
    US2 = "us2"
    AU1 = "au1"
    BR1 = "br1"
    IE1 = "ie1"
    JP1 = "jp1"
    SG1 = "sg1"
    IN1 = "in1"
    DE1 = "de1"
    GLL = "gll"

    __str__ = str.__str__


VideoParticipantSummaryEnumTwilioRealmOrStr: TypeAlias = Annotated[
    VideoParticipantSummaryEnumTwilioRealm | str, open_enum_validator(VideoParticipantSummaryEnumTwilioRealm)
]
