from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessagingV2RcsCarrierStatus(str, Enum):
    """The carrier-level status."""

    UNKNOWN = "UNKNOWN"
    UNLAUNCHED = "UNLAUNCHED"
    CARRIER_REVIEW = "CARRIER_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    SUSPENDED = "SUSPENDED"

    __str__ = str.__str__


MessagingV2RcsCarrierStatusOrStr: TypeAlias = Annotated[
    MessagingV2RcsCarrierStatus | str, open_enum_validator(MessagingV2RcsCarrierStatus)
]
