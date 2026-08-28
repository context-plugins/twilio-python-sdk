from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationMessageReceiptEnumDeliveryStatus(str, Enum):
    """The message delivery status, can be ``read``, ``failed``, ``delivered``, ``undelivered``, ``sent`` or null."""

    READ = "read"
    FAILED = "failed"
    DELIVERED = "delivered"
    UNDELIVERED = "undelivered"
    SENT = "sent"

    __str__ = str.__str__


ConversationMessageReceiptEnumDeliveryStatusOrStr: TypeAlias = Annotated[
    ConversationMessageReceiptEnumDeliveryStatus | str,
    open_enum_validator(ConversationMessageReceiptEnumDeliveryStatus),
]
