from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestType(str, Enum):
    NEW = "NEW"
    MIGRATION = "MIGRATION"
    LEASE = "LEASE"

    __str__ = str.__str__


RequestTypeOrStr: TypeAlias = Annotated[RequestType | str, open_enum_validator(RequestType)]
