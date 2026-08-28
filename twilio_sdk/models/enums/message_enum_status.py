from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumStatus(str, Enum):
    """The status of the Message. Possible values: ``accepted``, ``scheduled``, ``canceled``, ``queued``, ``sending``,
    ``sent``, ``failed``, ``delivered``, ``undelivered``, ``receiving``, ``received``, or ``read`` (WhatsApp only). For
    more information, See `detailed descriptions
    <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__."""

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


MessageEnumStatusOrStr: TypeAlias = Annotated[MessageEnumStatus | str, open_enum_validator(MessageEnumStatus)]
