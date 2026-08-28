from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingEnumFormat(str, Enum):
    MKA = "mka"
    MKV = "mkv"

    __str__ = str.__str__


RecordingEnumFormatOrStr: TypeAlias = Annotated[RecordingEnumFormat | str, open_enum_validator(RecordingEnumFormat)]
