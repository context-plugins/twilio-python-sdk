from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelAppEnumType(str, Enum):
    TRANSCRIPTION = "transcription"
    STUDIO = "studio"
    COPILOT = "copilot"

    __str__ = str.__str__


InteractionChannelAppEnumTypeOrStr: TypeAlias = Annotated[
    InteractionChannelAppEnumType | str, open_enum_validator(InteractionChannelAppEnumType)
]
