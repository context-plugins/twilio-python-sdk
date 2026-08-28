from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InsightsConversationalAiEnumSortBy(str, Enum):
    RECORD_COUNT = "record_count"
    SCORED_COUNT = "scored_count"
    TOTAL = "total"
    MEAN = "mean"
    SCORED_MEAN = "scored_mean"
    SCORE = "score"

    __str__ = str.__str__


InsightsConversationalAiEnumSortByOrStr: TypeAlias = Annotated[
    InsightsConversationalAiEnumSortBy | str, open_enum_validator(InsightsConversationalAiEnumSortBy)
]
