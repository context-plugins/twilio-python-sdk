from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WaitMethod(str, Enum):
    """The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default is ``POST``. When
    using a static audio file, this should be ``GET`` so that we can cache the file."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


WaitMethodOrStr: TypeAlias = Annotated[WaitMethod | str, open_enum_validator(WaitMethod)]
