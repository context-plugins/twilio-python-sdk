from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingStatusCallbackMethod2(str, Enum):
    """The HTTP method we should use when we call ``recording_status_callback``. Can be: ``GET`` or ``POST`` and
    defaults to ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


RecordingStatusCallbackMethod2OrStr: TypeAlias = Annotated[
    RecordingStatusCallbackMethod2 | str, open_enum_validator(RecordingStatusCallbackMethod2)
]
