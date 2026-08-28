from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AnnotationEnumConnectivityIssue(str, Enum):
    UNKNOWN_CONNECTIVITY_ISSUE = "unknown_connectivity_issue"
    NO_CONNECTIVITY_ISSUE = "no_connectivity_issue"
    INVALID_NUMBER = "invalid_number"
    CALLER_ID = "caller_id"
    DROPPED_CALL = "dropped_call"
    NUMBER_REACHABILITY = "number_reachability"

    __str__ = str.__str__


AnnotationEnumConnectivityIssueOrStr: TypeAlias = Annotated[
    AnnotationEnumConnectivityIssue | str, open_enum_validator(AnnotationEnumConnectivityIssue)
]
