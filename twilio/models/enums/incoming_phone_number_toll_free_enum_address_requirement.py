from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberTollFreeEnumAddressRequirement(str, Enum):
    """Whether the phone number requires an `Address <https://www.twilio.com/docs/usage/api/address>`__ registered with
    Twilio. Can be: ``none``, ``any``, ``local``, or ``foreign``."""

    NONE = "none"
    ANY = "any"
    LOCAL = "local"
    FOREIGN = "foreign"

    __str__ = str.__str__


IncomingPhoneNumberTollFreeEnumAddressRequirementOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberTollFreeEnumAddressRequirement | str,
    open_enum_validator(IncomingPhoneNumberTollFreeEnumAddressRequirement),
]
