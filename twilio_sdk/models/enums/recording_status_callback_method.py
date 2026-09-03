from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingStatusCallbackMethod(str, Enum):
    """The HTTP method we should use when calling the ``recording_status_callback`` URL. Can be: ``GET`` or ``POST`` and
    the default is ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


RecordingStatusCallbackMethodOrStr: TypeAlias = Annotated[
    RecordingStatusCallbackMethod | str, open_enum_validator(RecordingStatusCallbackMethod)
]
