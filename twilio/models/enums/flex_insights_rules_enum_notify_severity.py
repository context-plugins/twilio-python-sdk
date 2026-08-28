from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlexInsightsRulesEnumNotifySeverity(str, Enum):
    """The minimum severity level that will trigger a notification."""

    CRITICAL = "Critical"
    WARNING = "Warning"

    __str__ = str.__str__


FlexInsightsRulesEnumNotifySeverityOrStr: TypeAlias = Annotated[
    FlexInsightsRulesEnumNotifySeverity | str, open_enum_validator(FlexInsightsRulesEnumNotifySeverity)
]
