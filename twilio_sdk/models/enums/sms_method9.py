from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsMethod9(str, Enum):
    """The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults to ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsMethod9OrStr: TypeAlias = Annotated[SmsMethod9 | str, open_enum_validator(SmsMethod9)]
