from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InsightsConversationalAiEnumGranularity(str, Enum):
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    QUARTERS = "quarters"
    YEARS = "years"

    __str__ = str.__str__


InsightsConversationalAiEnumGranularityOrStr: TypeAlias = Annotated[
    InsightsConversationalAiEnumGranularity | str, open_enum_validator(InsightsConversationalAiEnumGranularity)
]
