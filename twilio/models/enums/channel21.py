from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel21(str, Enum):
    """Channel type for sending communications. Note: VOICE is receive-only and not supported for send operations."""

    SMS = "SMS"
    RCS = "RCS"
    WHATSAPP = "WHATSAPP"
    CHAT = "CHAT"

    __str__ = str.__str__


Channel21OrStr: TypeAlias = Annotated[Channel21 | str, open_enum_validator(Channel21)]
