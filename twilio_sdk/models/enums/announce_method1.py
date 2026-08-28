from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AnnounceMethod1(str, Enum):
    """The HTTP method we should use to call ``announce_url``. Can be: ``GET`` or ``POST`` and defaults to ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


AnnounceMethod1OrStr: TypeAlias = Annotated[AnnounceMethod1 | str, open_enum_validator(AnnounceMethod1)]
