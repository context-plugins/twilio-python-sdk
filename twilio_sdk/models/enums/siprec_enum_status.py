from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SiprecEnumStatus(str, Enum):
    """The status - one of ``stopped``, ``in-progress``"""

    IN_PROGRESS = "in-progress"
    STOPPED = "stopped"

    __str__ = str.__str__


SiprecEnumStatusOrStr: TypeAlias = Annotated[SiprecEnumStatus | str, open_enum_validator(SiprecEnumStatus)]
