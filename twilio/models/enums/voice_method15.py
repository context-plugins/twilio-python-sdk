from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceMethod15(str, Enum):
    """The HTTP method we should use to call ``voice_url``"""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceMethod15OrStr: TypeAlias = Annotated[VoiceMethod15 | str, open_enum_validator(VoiceMethod15)]
