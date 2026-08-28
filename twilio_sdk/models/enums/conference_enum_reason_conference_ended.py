from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumReasonConferenceEnded(str, Enum):
    """The reason why a conference ended. When a conference is in progress, will be ``null``. When conference is
    completed, can be: ``conference-ended-via-api``, ``participant-with-end-conference-on-exit-left``,
    ``participant-with-end-conference-on-exit-kicked``, ``last-participant-kicked``, or ``last-participant-left``."""

    CONFERENCE_ENDED_VIA_API = "conference-ended-via-api"
    PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_LEFT = "participant-with-end-conference-on-exit-left"
    PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_KICKED = "participant-with-end-conference-on-exit-kicked"
    LAST_PARTICIPANT_KICKED = "last-participant-kicked"
    LAST_PARTICIPANT_LEFT = "last-participant-left"

    __str__ = str.__str__


ConferenceEnumReasonConferenceEndedOrStr: TypeAlias = Annotated[
    ConferenceEnumReasonConferenceEnded | str, open_enum_validator(ConferenceEnumReasonConferenceEnded)
]
