from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceStatusCallbackMethod(str, Enum):
    """The HTTP method we should use to call ``conference_status_callback``. Can be: ``GET`` or ``POST`` and defaults to
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


ConferenceStatusCallbackMethodOrStr: TypeAlias = Annotated[
    ConferenceStatusCallbackMethod | str, open_enum_validator(ConferenceStatusCallbackMethod)
]
