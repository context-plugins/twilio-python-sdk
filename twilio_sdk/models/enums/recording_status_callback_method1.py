from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingStatusCallbackMethod1(str, Enum):
    """The HTTP method we should use to call ``recording_status_callback``. Can be: ``GET`` or ``POST`` and the default
    is ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


RecordingStatusCallbackMethod1OrStr: TypeAlias = Annotated[
    RecordingStatusCallbackMethod1 | str, open_enum_validator(RecordingStatusCallbackMethod1)
]
