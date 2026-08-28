from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel4(str, Enum):
    """Channel type. Required when participantId has multiple addresses or when using explicit address."""

    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel4OrStr: TypeAlias = Annotated[Channel4 | str, open_enum_validator(Channel4)]
