from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountEnumType(str, Enum):
    """The type of this account. Either ``Trial`` or ``Full`` if it's been upgraded"""

    TRIAL = "Trial"
    FULL = "Full"

    __str__ = str.__str__


AccountEnumTypeOrStr: TypeAlias = Annotated[AccountEnumType | str, open_enum_validator(AccountEnumType)]
