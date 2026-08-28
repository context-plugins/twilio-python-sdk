from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceConversationMessageReceiptEnumDeliveryStatus(str, Enum):
    """The message delivery status, can be ``read``, ``failed``, ``delivered``, ``undelivered``, ``sent`` or null."""

    READ = "read"
    FAILED = "failed"
    DELIVERED = "delivered"
    UNDELIVERED = "undelivered"
    SENT = "sent"

    __str__ = str.__str__


ServiceConversationMessageReceiptEnumDeliveryStatusOrStr: TypeAlias = Annotated[
    ServiceConversationMessageReceiptEnumDeliveryStatus | str,
    open_enum_validator(ServiceConversationMessageReceiptEnumDeliveryStatus),
]
