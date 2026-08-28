from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationAttemptEnumChannels(str, Enum):
    """A string specifying the communication channel used for the verification attempt."""

    SMS = "sms"
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    RBM = "rbm"

    __str__ = str.__str__


VerificationAttemptEnumChannelsOrStr: TypeAlias = Annotated[
    VerificationAttemptEnumChannels | str, open_enum_validator(VerificationAttemptEnumChannels)
]
