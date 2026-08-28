from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingEnumType(str, Enum):
    """The recording's media type. Can be: ``audio`` or ``video``."""

    AUDIO = "audio"
    VIDEO = "video"
    DATA = "data"

    __str__ = str.__str__


RecordingEnumTypeOrStr: TypeAlias = Annotated[RecordingEnumType | str, open_enum_validator(RecordingEnumType)]
