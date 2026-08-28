from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AnnounceMethod(str, Enum):
    """The HTTP method used to call ``announce_url``. Can be: ``GET`` or ``POST`` and the default is ``POST``"""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


AnnounceMethodOrStr: TypeAlias = Annotated[AnnounceMethod | str, open_enum_validator(AnnounceMethod)]
