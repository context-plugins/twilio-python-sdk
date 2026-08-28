from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod8(str, Enum):
    """The HTTP method we should use when calling the ``status_callback`` URL. Can be: ``GET`` or ``POST`` and the
    default is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod8OrStr: TypeAlias = Annotated[
    StatusCallbackMethod8 | str, open_enum_validator(StatusCallbackMethod8)
]
