from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel2(str, Enum):
    """The channel for Communication."""

    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel2OrStr: TypeAlias = Annotated[Channel2 | str, open_enum_validator(Channel2)]
