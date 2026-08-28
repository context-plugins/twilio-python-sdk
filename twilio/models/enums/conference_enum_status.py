from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumStatus(str, Enum):
    """The status of this conference. Can be: ``init``, ``in-progress``, or ``completed``."""

    INIT = "init"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

    __str__ = str.__str__


ConferenceEnumStatusOrStr: TypeAlias = Annotated[ConferenceEnumStatus | str, open_enum_validator(ConferenceEnumStatus)]
