from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationEnumChannel(str, Enum):
    """The verification method used. One of: https://www.twilio.com/docs/verify/email, ``sms``, ``whatsapp``, ``call``,
    ``sna``, or ``rcs``."""

    SMS = "sms"
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    SNA = "sna"

    __str__ = str.__str__


VerificationEnumChannelOrStr: TypeAlias = Annotated[
    VerificationEnumChannel | str, open_enum_validator(VerificationEnumChannel)
]
