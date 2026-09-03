from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewFactorEnumFactorTypes(str, Enum):
    """The Type of this Factor. Currently ``push`` and ``totp`` are supported."""

    PUSH = "push"
    TOTP = "totp"
    PASSKEYS = "passkeys"

    __str__ = str.__str__


NewFactorEnumFactorTypesOrStr: TypeAlias = Annotated[
    NewFactorEnumFactorTypes | str, open_enum_validator(NewFactorEnumFactorTypes)
]
