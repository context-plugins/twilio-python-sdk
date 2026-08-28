from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConnectAppEnumPermission(str, Enum):
    """The set of permissions that your ConnectApp requests."""

    GET_ALL = "get-all"
    POST_ALL = "post-all"

    __str__ = str.__str__


ConnectAppEnumPermissionOrStr: TypeAlias = Annotated[
    ConnectAppEnumPermission | str, open_enum_validator(ConnectAppEnumPermission)
]
