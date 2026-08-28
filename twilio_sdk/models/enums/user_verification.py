from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserVerification(str, Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    DISCOURAGED = "discouraged"

    __str__ = str.__str__


UserVerificationOrStr: TypeAlias = Annotated[UserVerification | str, open_enum_validator(UserVerification)]
