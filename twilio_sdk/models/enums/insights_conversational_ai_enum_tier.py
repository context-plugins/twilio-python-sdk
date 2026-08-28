from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InsightsConversationalAiEnumTier(str, Enum):
    LOW = "Low"
    HIGH = "High"
    NEUTRAL = "Neutral"

    __str__ = str.__str__


InsightsConversationalAiEnumTierOrStr: TypeAlias = Annotated[
    InsightsConversationalAiEnumTier | str, open_enum_validator(InsightsConversationalAiEnumTier)
]
