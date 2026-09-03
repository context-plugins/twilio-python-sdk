from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FactorEnumNotificationPlatforms(str, Enum):
    APN = "apn"
    FCM = "fcm"
    NONE = "none"

    __str__ = str.__str__


FactorEnumNotificationPlatformsOrStr: TypeAlias = Annotated[
    FactorEnumNotificationPlatforms | str, open_enum_validator(FactorEnumNotificationPlatforms)
]
