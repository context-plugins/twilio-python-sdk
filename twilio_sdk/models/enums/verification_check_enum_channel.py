from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationCheckEnumChannel(str, Enum):
    """The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``, ``whatsapp``,
    ``call``, or ``sna``."""

    SMS = "sms"
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    SNA = "sna"

    __str__ = str.__str__


VerificationCheckEnumChannelOrStr: TypeAlias = Annotated[
    VerificationCheckEnumChannel | str, open_enum_validator(VerificationCheckEnumChannel)
]
