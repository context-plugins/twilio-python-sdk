from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberTollFreeEnumEmergencyAddressStatus(str, Enum):
    """The status of address registration with emergency services. A registered emergency address will be used during
    handling of emergency calls from this number."""

    REGISTERED = "registered"
    UNREGISTERED = "unregistered"
    PENDING_REGISTRATION = "pending-registration"
    REGISTRATION_FAILURE = "registration-failure"
    PENDING_UNREGISTRATION = "pending-unregistration"
    UNREGISTRATION_FAILURE = "unregistration-failure"

    __str__ = str.__str__


IncomingPhoneNumberTollFreeEnumEmergencyAddressStatusOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberTollFreeEnumEmergencyAddressStatus | str,
    open_enum_validator(IncomingPhoneNumberTollFreeEnumEmergencyAddressStatus),
]
