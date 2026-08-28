from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticationActionType(str, Enum):
    COPY_CODE = "COPY_CODE"

    __str__ = str.__str__


AuthenticationActionTypeOrStr: TypeAlias = Annotated[
    AuthenticationActionType | str, open_enum_validator(AuthenticationActionType)
]
