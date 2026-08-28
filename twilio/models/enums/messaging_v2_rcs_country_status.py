from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessagingV2RcsCountryStatus(str, Enum):
    """The country-level status. Based on the aggregation of the carrier-level status."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    TWILIO_REVIEW = "TWILIO_REVIEW"
    PENDING_VERIFICATION = "PENDING_VERIFICATION"

    __str__ = str.__str__


MessagingV2RcsCountryStatusOrStr: TypeAlias = Annotated[
    MessagingV2RcsCountryStatus | str, open_enum_validator(MessagingV2RcsCountryStatus)
]
