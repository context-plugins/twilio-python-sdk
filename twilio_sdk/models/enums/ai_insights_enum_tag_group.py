from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AiInsightsEnumTagGroup(str, Enum):
    TOPICS = "topics"

    __str__ = str.__str__


AiInsightsEnumTagGroupOrStr: TypeAlias = Annotated[
    AiInsightsEnumTagGroup | str, open_enum_validator(AiInsightsEnumTagGroup)
]
