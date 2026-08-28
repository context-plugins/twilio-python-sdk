from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InsightsConversationalAiEnumName(str, Enum):
    PREDICTIVE_SCORES = "predictive_scores"
    CHANNEL_METRICS = "channel_metrics"
    AGENT_METRICS = "agent_metrics"
    QUEUE_METRICS = "queue_metrics"
    AGENTS_CSAT_SUMMARY = "agents_csat_summary"
    TOPIC_METRICS = "topic_metrics"
    CONVERSATION_METRICS = "conversation_metrics"
    TREND_METRICS = "trend_metrics"

    __str__ = str.__str__


InsightsConversationalAiEnumNameOrStr: TypeAlias = Annotated[
    InsightsConversationalAiEnumName | str, open_enum_validator(InsightsConversationalAiEnumName)
]
