from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMethod14(str, Enum):
    """The HTTP method we should use when calling the ``sms_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsMethod14OrStr: TypeAlias = Annotated[SmsMethod14 | str, open_enum_validator(SmsMethod14)]
