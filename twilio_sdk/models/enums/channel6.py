from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel6(str, Enum):
    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel6OrStr: TypeAlias = Annotated[Channel6 | str, open_enum_validator(Channel6)]
