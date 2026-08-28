from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FactorEnumFactorTypes(str, Enum):
    """The Type of this Factor. Currently ``push`` and ``totp`` are supported."""

    PUSH = "push"
    TOTP = "totp"
    PASSKEYS = "passkeys"

    __str__ = str.__str__


FactorEnumFactorTypesOrStr: TypeAlias = Annotated[
    FactorEnumFactorTypes | str, open_enum_validator(FactorEnumFactorTypes)
]
