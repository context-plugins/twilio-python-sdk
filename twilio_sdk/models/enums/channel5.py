from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel5(str, Enum):
    VOICE = "VOICE"
    SMS = "SMS"
    RCS = "RCS"
    EMAIL = "EMAIL"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"
    API = "API"
    SYSTEM = "SYSTEM"

    __str__ = str.__str__


Channel5OrStr: TypeAlias = Annotated[Channel5 | str, open_enum_validator(Channel5)]
