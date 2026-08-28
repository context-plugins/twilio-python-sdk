from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DiscoverableCredentials(str, Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    DISCOURAGED = "discouraged"

    __str__ = str.__str__


DiscoverableCredentialsOrStr: TypeAlias = Annotated[
    DiscoverableCredentials | str, open_enum_validator(DiscoverableCredentials)
]
