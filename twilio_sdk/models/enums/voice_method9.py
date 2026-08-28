from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceMethod9(str, Enum):
    """The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and defaults to
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceMethod9OrStr: TypeAlias = Annotated[VoiceMethod9 | str, open_enum_validator(VoiceMethod9)]
