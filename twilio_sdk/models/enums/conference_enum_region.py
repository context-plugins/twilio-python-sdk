from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumRegion(str, Enum):
    US1 = "us1"
    US2 = "us2"
    AU1 = "au1"
    BR1 = "br1"
    IE1 = "ie1"
    JP1 = "jp1"
    SG1 = "sg1"
    DE1 = "de1"
    IN1 = "in1"

    __str__ = str.__str__


ConferenceEnumRegionOrStr: TypeAlias = Annotated[ConferenceEnumRegion | str, open_enum_validator(ConferenceEnumRegion)]
