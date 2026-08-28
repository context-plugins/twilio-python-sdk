from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumTag(str, Enum):
    INVALID_REQUESTED_REGION = "invalid_requested_region"
    DUPLICATE_IDENTITY = "duplicate_identity"
    START_FAILURE = "start_failure"
    REGION_CONFIGURATION_ISSUES = "region_configuration_issues"
    QUALITY_WARNINGS = "quality_warnings"
    PARTICIPANT_BEHAVIOR_ISSUES = "participant_behavior_issues"
    HIGH_PACKET_LOSS = "high_packet_loss"
    HIGH_JITTER = "high_jitter"
    HIGH_LATENCY = "high_latency"
    LOW_MOS = "low_mos"
    DETECTED_SILENCE = "detected_silence"
    NO_CONCURRENT_PARTICIPANTS = "no_concurrent_participants"

    __str__ = str.__str__


ConferenceEnumTagOrStr: TypeAlias = Annotated[ConferenceEnumTag | str, open_enum_validator(ConferenceEnumTag)]
