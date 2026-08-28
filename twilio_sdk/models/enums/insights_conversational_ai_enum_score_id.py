from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InsightsConversationalAiEnumScoreId(str, Enum):
    PREDICTED_CSAT = "~predicted-csat"
    AGENT_EXPERIENCE = "~agent-experience"
    CUSTOMER_EFFORT = "~customer-effort"
    MULTITOUCH_RISK = "~multitouch-risk"

    __str__ = str.__str__


InsightsConversationalAiEnumScoreIdOrStr: TypeAlias = Annotated[
    InsightsConversationalAiEnumScoreId | str, open_enum_validator(InsightsConversationalAiEnumScoreId)
]
