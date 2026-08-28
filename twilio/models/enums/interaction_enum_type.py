from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionEnumType(str, Enum):
    """The Type of the Interaction. Can be: ``message``, ``voice`` or ``unknown``."""

    MESSAGE = "message"
    VOICE = "voice"
    UNKNOWN = "unknown"

    __str__ = str.__str__


InteractionEnumTypeOrStr: TypeAlias = Annotated[InteractionEnumType | str, open_enum_validator(InteractionEnumType)]
