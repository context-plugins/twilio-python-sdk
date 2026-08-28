from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RejectionReason(str, Enum):
    """The description of the rejection reason provided by the losing carrier. This field may be null if the number has
    not been rejected by the losing carrier."""

    CONTACT_SUPPORT_REQUIRED = "CONTACT_SUPPORT_REQUIRED"
    PHONE_NUMBER_WITH_CARRIER_RESTRICTION = "PHONE_NUMBER_WITH_CARRIER_RESTRICTION"
    PHONE_NUMBER_INACTIVE_OR_DISCONNECTED = "PHONE_NUMBER_INACTIVE_OR_DISCONNECTED"
    INVALID_END_USER_NAME = "INVALID_END_USER_NAME"
    INVALID_ADDRESS = "INVALID_ADDRESS"
    INVALID_PIN = "INVALID_PIN"
    INVALID_ACCOUNT_NUMBER = "INVALID_ACCOUNT_NUMBER"

    __str__ = str.__str__


RejectionReasonOrStr: TypeAlias = Annotated[RejectionReason | str, open_enum_validator(RejectionReason)]
