from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumDirection(str, Enum):
    """The direction of the message. Can be: ``inbound`` for incoming messages, ``outbound-api`` for messages created by
    the REST API, ``outbound-call`` for messages created during a call, or ``outbound-reply`` for messages created in
    response to an incoming message."""

    INBOUND = "inbound"
    OUTBOUND_API = "outbound-api"
    OUTBOUND_CALL = "outbound-call"
    OUTBOUND_REPLY = "outbound-reply"

    __str__ = str.__str__


MessageEnumDirectionOrStr: TypeAlias = Annotated[MessageEnumDirection | str, open_enum_validator(MessageEnumDirection)]
