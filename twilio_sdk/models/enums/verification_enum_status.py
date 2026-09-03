from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationEnumStatus(str, Enum):
    """The status of the verification. Can be: ``pending``, ``approved``, ``canceled``, ``max_attempts_reached``,
    ``deleted``, ``failed`` or ``expired``."""

    CANCELED = "canceled"
    APPROVED = "approved"

    __str__ = str.__str__


VerificationEnumStatusOrStr: TypeAlias = Annotated[
    VerificationEnumStatus | str, open_enum_validator(VerificationEnumStatus)
]
