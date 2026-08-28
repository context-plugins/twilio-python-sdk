from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeliveryStatus(str, Enum):
    """Delivery status of the Communication to this recipient."""

    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    DELIVERED = "DELIVERED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    __str__ = str.__str__


DeliveryStatusOrStr: TypeAlias = Annotated[DeliveryStatus | str, open_enum_validator(DeliveryStatus)]
