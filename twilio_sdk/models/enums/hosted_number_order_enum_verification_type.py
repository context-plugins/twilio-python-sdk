from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HostedNumberOrderEnumVerificationType(str, Enum):
    """The method used to verify ownership of the number to be hosted. Can be: ``phone-call`` or ``phone-bill`` and the
    default is ``phone-call``."""

    PHONE_CALL = "phone-call"
    PHONE_BILL = "phone-bill"

    __str__ = str.__str__


HostedNumberOrderEnumVerificationTypeOrStr: TypeAlias = Annotated[
    HostedNumberOrderEnumVerificationType | str, open_enum_validator(HostedNumberOrderEnumVerificationType)
]
