from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel1(str, Enum):
    """The messaging channel. Must be "WHATSAPP"."""

    WHATSAPP = "WHATSAPP"

    __str__ = str.__str__


Channel1OrStr: TypeAlias = Annotated[Channel1 | str, open_enum_validator(Channel1)]
