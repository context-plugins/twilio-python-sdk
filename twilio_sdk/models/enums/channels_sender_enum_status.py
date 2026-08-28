from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChannelsSenderEnumStatus(str, Enum):
    """The status of the sender."""

    CREATING = "CREATING"
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    VERIFYING = "VERIFYING"
    ONLINE_UPDATING = "ONLINE:UPDATING"
    TWILIO_REVIEW = "TWILIO_REVIEW"
    DRAFT = "DRAFT"
    STUBBED = "STUBBED"

    __str__ = str.__str__


ChannelsSenderEnumStatusOrStr: TypeAlias = Annotated[
    ChannelsSenderEnumStatus | str, open_enum_validator(ChannelsSenderEnumStatus)
]
