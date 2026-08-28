from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccessTokenEnumFactorTypes(str, Enum):
    """The Type of the Factor. Currently only ``push`` is supported."""

    PUSH = "push"

    __str__ = str.__str__


AccessTokenEnumFactorTypesOrStr: TypeAlias = Annotated[
    AccessTokenEnumFactorTypes | str, open_enum_validator(AccessTokenEnumFactorTypes)
]
