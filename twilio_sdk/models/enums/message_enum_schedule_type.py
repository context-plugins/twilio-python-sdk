from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumScheduleType(str, Enum):
    """For Messaging Services only: Include this parameter with a value of ``fixed`` in conjuction with the
    ``send_time`` parameter in order to `schedule a Message
    <https://www.twilio.com/docs/messaging/features/message-scheduling>`__."""

    FIXED = "fixed"

    __str__ = str.__str__


MessageEnumScheduleTypeOrStr: TypeAlias = Annotated[
    MessageEnumScheduleType | str, open_enum_validator(MessageEnumScheduleType)
]
