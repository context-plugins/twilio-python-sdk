from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMessageEnumStatus(str, Enum):
    QUEUED = "queued"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"
    DELIVERED = "delivered"
    UNDELIVERED = "undelivered"
    RECEIVING = "receiving"
    RECEIVED = "received"
    ACCEPTED = "accepted"
    SCHEDULED = "scheduled"
    READ = "read"
    PARTIALLY_DELIVERED = "partially_delivered"
    CANCELED = "canceled"

    __str__ = str.__str__


SmsMessageEnumStatusOrStr: TypeAlias = Annotated[SmsMessageEnumStatus | str, open_enum_validator(SmsMessageEnumStatus)]
