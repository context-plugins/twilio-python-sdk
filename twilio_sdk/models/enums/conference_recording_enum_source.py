from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceRecordingEnumSource(str, Enum):
    """How the recording was created. Can be: ``DialVerb``, ``Conference``, ``OutboundAPI``, ``Trunking``,
    ``RecordVerb``, ``StartCallRecordingAPI``, ``StartConferenceRecordingAPI``."""

    DIAL_VERB = "DialVerb"
    CONFERENCE = "Conference"
    OUTBOUND_API = "OutboundAPI"
    TRUNKING = "Trunking"
    RECORD_VERB = "RecordVerb"
    START_CALL_RECORDING_API = "StartCallRecordingAPI"
    START_CONFERENCE_RECORDING_API = "StartConferenceRecordingAPI"

    __str__ = str.__str__


ConferenceRecordingEnumSourceOrStr: TypeAlias = Annotated[
    ConferenceRecordingEnumSource | str, open_enum_validator(ConferenceRecordingEnumSource)
]
