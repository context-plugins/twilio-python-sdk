from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Method21(str, Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    __str__ = str.__str__


Method21OrStr: TypeAlias = Annotated[Method21 | str, open_enum_validator(Method21)]
