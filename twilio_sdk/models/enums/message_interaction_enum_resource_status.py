from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageInteractionEnumResourceStatus(str, Enum):
    """Always empty for created Message Interactions."""

    ACCEPTED = "accepted"
    ANSWERED = "answered"
    BUSY = "busy"
    CANCELED = "canceled"
    COMPLETED = "completed"
    DELETED = "deleted"
    DELIVERED = "delivered"
    DELIVERY_UNKNOWN = "delivery-unknown"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    INITIATED = "initiated"
    NO_ANSWER = "no-answer"
    QUEUED = "queued"
    RECEIVED = "received"
    RECEIVING = "receiving"
    RINGING = "ringing"
    SCHEDULED = "scheduled"
    SENDING = "sending"
    SENT = "sent"
    UNDELIVERED = "undelivered"
    UNKNOWN = "unknown"

    __str__ = str.__str__


MessageInteractionEnumResourceStatusOrStr: TypeAlias = Annotated[
    MessageInteractionEnumResourceStatus | str, open_enum_validator(MessageInteractionEnumResourceStatus)
]
