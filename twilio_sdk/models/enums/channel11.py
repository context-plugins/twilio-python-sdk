from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel11(str, Enum):
    """Channel type for the Participant address."""

    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel11OrStr: TypeAlias = Annotated[Channel11 | str, open_enum_validator(Channel11)]
