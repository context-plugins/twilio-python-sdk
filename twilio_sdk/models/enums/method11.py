from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Method11(str, Enum):
    """The HTTP method used to invoke the webhook URL."""

    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    __str__ = str.__str__


Method11OrStr: TypeAlias = Annotated[Method11 | str, open_enum_validator(Method11)]
