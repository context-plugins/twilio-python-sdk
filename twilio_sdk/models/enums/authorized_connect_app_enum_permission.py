from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthorizedConnectAppEnumPermission(str, Enum):
    """The set of permissions that you authorized for the Connect App. Can be: ``get-all`` or ``post-all``."""

    GET_ALL = "get-all"
    POST_ALL = "post-all"

    __str__ = str.__str__


AuthorizedConnectAppEnumPermissionOrStr: TypeAlias = Annotated[
    AuthorizedConnectAppEnumPermission | str, open_enum_validator(AuthorizedConnectAppEnumPermission)
]
