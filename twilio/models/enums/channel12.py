from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel12(str, Enum):
    """Channel type for the Participant address."""

    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel12OrStr: TypeAlias = Annotated[Channel12 | str, open_enum_validator(Channel12)]
