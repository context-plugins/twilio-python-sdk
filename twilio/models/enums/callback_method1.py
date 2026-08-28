from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackMethod1(str, Enum):
    """The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the default is
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


CallbackMethod1OrStr: TypeAlias = Annotated[CallbackMethod1 | str, open_enum_validator(CallbackMethod1)]
