from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HostedNumberOrderEnumVerificationType1(str, Enum):
    """The method used to verify ownership of the number to be hosted. Can be: ``phone-call`` or ``phone-bill`` and the
    default is ``phone-call``."""

    PHONE_CALL = "phone-call"

    __str__ = str.__str__


HostedNumberOrderEnumVerificationType1OrStr: TypeAlias = Annotated[
    HostedNumberOrderEnumVerificationType1 | str, open_enum_validator(HostedNumberOrderEnumVerificationType1)
]
