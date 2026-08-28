from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceBindingEnumBindingType(str, Enum):
    """The push technology to use for the Binding. Can be: ``apn``, ``gcm``, ``fcm``, or ``twilsock``. See `push
    notification configuration <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info."""

    APN = "apn"
    GCM = "gcm"
    FCM = "fcm"
    TWILSOCK = "twilsock"

    __str__ = str.__str__


ServiceBindingEnumBindingTypeOrStr: TypeAlias = Annotated[
    ServiceBindingEnumBindingType | str, open_enum_validator(ServiceBindingEnumBindingType)
]
