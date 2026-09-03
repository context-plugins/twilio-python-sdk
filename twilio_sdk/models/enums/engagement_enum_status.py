from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EngagementEnumStatus(str, Enum):
    """The status of the Engagement. Can be: ``active`` or ``ended``., The status of the Execution. Can be: ``active``
    or ``ended``."""

    ACTIVE = "active"
    ENDED = "ended"

    __str__ = str.__str__


EngagementEnumStatusOrStr: TypeAlias = Annotated[EngagementEnumStatus | str, open_enum_validator(EngagementEnumStatus)]
