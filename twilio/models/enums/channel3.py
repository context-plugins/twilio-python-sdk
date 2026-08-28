from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel3(str, Enum):
    """Channel type for address resolution."""

    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel3OrStr: TypeAlias = Annotated[Channel3 | str, open_enum_validator(Channel3)]
