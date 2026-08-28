from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMethod(str, Enum):
    """The HTTP method we use to call ``sms_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsMethodOrStr: TypeAlias = Annotated[SmsMethod | str, open_enum_validator(SmsMethod)]
