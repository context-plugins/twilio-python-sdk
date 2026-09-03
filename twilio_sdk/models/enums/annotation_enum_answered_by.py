from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AnnotationEnumAnsweredBy(str, Enum):
    UNKNOWN_ANSWERED_BY = "unknown_answered_by"
    HUMAN = "human"
    MACHINE = "machine"

    __str__ = str.__str__


AnnotationEnumAnsweredByOrStr: TypeAlias = Annotated[
    AnnotationEnumAnsweredBy | str, open_enum_validator(AnnotationEnumAnsweredBy)
]
