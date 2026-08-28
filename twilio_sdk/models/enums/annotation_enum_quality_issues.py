from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AnnotationEnumQualityIssues(str, Enum):
    UNKNOWN_QUALITY_ISSUE = "unknown_quality_issue"
    NO_QUALITY_ISSUE = "no_quality_issue"
    LOW_VOLUME = "low_volume"
    CHOPPY_ROBOTIC = "choppy_robotic"
    ECHO = "echo"
    DTMF = "dtmf"
    LATENCY = "latency"
    OWA = "owa"
    STATIC_NOISE = "static_noise"

    __str__ = str.__str__


AnnotationEnumQualityIssuesOrStr: TypeAlias = Annotated[
    AnnotationEnumQualityIssues | str, open_enum_validator(AnnotationEnumQualityIssues)
]
