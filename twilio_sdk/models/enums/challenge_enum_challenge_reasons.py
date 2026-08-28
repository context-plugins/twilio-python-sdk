from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeEnumChallengeReasons(str, Enum):
    """Reason for the Challenge to be in certain ``status``. One of ``none``, ``not_needed`` or ``not_requested``."""

    NONE = "none"
    NOT_NEEDED = "not_needed"
    NOT_REQUESTED = "not_requested"

    __str__ = str.__str__


ChallengeEnumChallengeReasonsOrStr: TypeAlias = Annotated[
    ChallengeEnumChallengeReasons | str, open_enum_validator(ChallengeEnumChallengeReasons)
]
