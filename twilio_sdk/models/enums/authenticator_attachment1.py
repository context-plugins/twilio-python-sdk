from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticatorAttachment1(str, Enum):
    PLATFORM = "platform"
    CROSS_PLATFORM = "cross-platform"
    ANY = "any"

    __str__ = str.__str__


AuthenticatorAttachment1OrStr: TypeAlias = Annotated[
    AuthenticatorAttachment1 | str, open_enum_validator(AuthenticatorAttachment1)
]
