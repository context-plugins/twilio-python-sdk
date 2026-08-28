from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberMobileEnumEmergencyStatus(str, Enum):
    """The parameter displays if emergency calling is enabled for this number. Active numbers may place emergency calls
    by dialing valid emergency numbers for the country."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"

    __str__ = str.__str__


IncomingPhoneNumberMobileEnumEmergencyStatusOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberMobileEnumEmergencyStatus | str,
    open_enum_validator(IncomingPhoneNumberMobileEnumEmergencyStatus),
]
