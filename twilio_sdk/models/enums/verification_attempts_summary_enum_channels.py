from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationAttemptsSummaryEnumChannels(str, Enum):
    SMS = "sms"
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    RBM = "rbm"

    __str__ = str.__str__


VerificationAttemptsSummaryEnumChannelsOrStr: TypeAlias = Annotated[
    VerificationAttemptsSummaryEnumChannels | str, open_enum_validator(VerificationAttemptsSummaryEnumChannels)
]
