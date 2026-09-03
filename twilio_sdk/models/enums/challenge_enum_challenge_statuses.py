from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeEnumChallengeStatuses(str, Enum):
    """The Status of this Challenge. One of ``pending``, ``expired``, ``approved`` or ``denied``."""

    PENDING = "pending"
    EXPIRED = "expired"
    APPROVED = "approved"
    DENIED = "denied"

    __str__ = str.__str__


ChallengeEnumChallengeStatusesOrStr: TypeAlias = Annotated[
    ChallengeEnumChallengeStatuses | str, open_enum_validator(ChallengeEnumChallengeStatuses)
]
