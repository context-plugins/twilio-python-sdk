from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeEnumFactorTypes(str, Enum):
    """The Factor Type of this Challenge. Currently ``push`` and ``totp`` are supported."""

    PUSH = "push"
    TOTP = "totp"
    PASSKEYS = "passkeys"

    __str__ = str.__str__


ChallengeEnumFactorTypesOrStr: TypeAlias = Annotated[
    ChallengeEnumFactorTypes | str, open_enum_validator(ChallengeEnumFactorTypes)
]
