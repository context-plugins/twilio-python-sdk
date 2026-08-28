from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CredentialEnumPushType(str, Enum):
    """The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``."""

    APN = "apn"
    GCM = "gcm"
    FCM = "fcm"

    __str__ = str.__str__


CredentialEnumPushTypeOrStr: TypeAlias = Annotated[
    CredentialEnumPushType | str, open_enum_validator(CredentialEnumPushType)
]
