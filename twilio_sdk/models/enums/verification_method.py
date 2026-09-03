from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationMethod(str, Enum):
    """The verification method."""

    SMS = "sms"
    VOICE = "voice"

    __str__ = str.__str__


VerificationMethodOrStr: TypeAlias = Annotated[VerificationMethod | str, open_enum_validator(VerificationMethod)]
