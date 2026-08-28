from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionEnumResourceStatus(str, Enum):
    """The inbound resource status of the Interaction. Will always be ``delivered`` for messages and ``in-progress`` for
    calls."""

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


InteractionEnumResourceStatusOrStr: TypeAlias = Annotated[
    InteractionEnumResourceStatus | str, open_enum_validator(InteractionEnumResourceStatus)
]
