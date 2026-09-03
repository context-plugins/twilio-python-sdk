from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewFactorEnumNotificationPlatforms(str, Enum):
    APN = "apn"
    FCM = "fcm"
    NONE = "none"

    __str__ = str.__str__


NewFactorEnumNotificationPlatformsOrStr: TypeAlias = Annotated[
    NewFactorEnumNotificationPlatforms | str, open_enum_validator(NewFactorEnumNotificationPlatforms)
]
