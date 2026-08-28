from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMethod6(str, Enum):
    """The HTTP method we use to call the ``sms_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsMethod6OrStr: TypeAlias = Annotated[SmsMethod6 | str, open_enum_validator(SmsMethod6)]
