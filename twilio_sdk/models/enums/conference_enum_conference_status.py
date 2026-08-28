from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumConferenceStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    NOT_STARTED = "not_started"
    COMPLETED = "completed"
    SUMMARY_TIMEOUT = "summary_timeout"

    __str__ = str.__str__


ConferenceEnumConferenceStatusOrStr: TypeAlias = Annotated[
    ConferenceEnumConferenceStatus | str, open_enum_validator(ConferenceEnumConferenceStatus)
]
