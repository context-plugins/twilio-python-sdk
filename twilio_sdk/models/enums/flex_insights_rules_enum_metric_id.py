from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlexInsightsRulesEnumMetricId(str, Enum):
    """The metric this rule is associated with."""

    ACTIVE_NOW = "Active (Now)"
    WAITING_NOW = "Waiting (Now)"
    AVAILABLE_AGENTS_NOW = "Available Agents (Now)"
    OFFLINE_AGENTS_NOW = "Offline Agents (Now)"
    UNAVAILABLE_AGENTS_NOW = "Unavailable Agents (Now)"
    ABANDONED_30_MIN = "Abandoned (30 min)"
    ABANDONED_TODAY = "Abandoned (Today)"
    ACCEPTED_30_MIN = "Accepted (30 min)"
    ACCEPTED_TODAY = "Accepted (Today)"
    AVG_SPEED_OF_ANSWER_TODAY = "Avg. Speed of Answer (Today)"
    AVG_HANDLE_TIME_TODAY = "Avg. Handle Time (Today)"
    MISSED_INVITATIONS_30_MIN = "Missed Invitations (30 min)"
    MISSED_INVITATIONS_TODAY = "Missed Invitations (Today)"
    SLA_30_MIN = "SLA (30 min)"
    SLA_TODAY = "SLA (Today)"
    LONGEST_AVAILABLE_AGENT_NOW = "Longest Available Agent (Now)"
    LONGEST_NOW = "Longest (Now)"

    __str__ = str.__str__


FlexInsightsRulesEnumMetricIdOrStr: TypeAlias = Annotated[
    FlexInsightsRulesEnumMetricId | str, open_enum_validator(FlexInsightsRulesEnumMetricId)
]
