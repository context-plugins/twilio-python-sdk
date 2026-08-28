from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DependentPhoneNumberEnumEmergencyStatus(str, Enum):
    """Whether the phone number is enabled for emergency calling."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"

    __str__ = str.__str__


DependentPhoneNumberEnumEmergencyStatusOrStr: TypeAlias = Annotated[
    DependentPhoneNumberEnumEmergencyStatus | str, open_enum_validator(DependentPhoneNumberEnumEmergencyStatus)
]
