from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumUpdateStatus(str, Enum):
    COMPLETED = "completed"

    __str__ = str.__str__


ConferenceEnumUpdateStatusOrStr: TypeAlias = Annotated[
    ConferenceEnumUpdateStatus | str, open_enum_validator(ConferenceEnumUpdateStatus)
]
