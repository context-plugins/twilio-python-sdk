from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HostedNumberOrderEnumStatus(str, Enum):
    """The status of the hosted number order. Can be: ``twilio-processing``, ``received``, ``pending-verification``,
    ``verified``, ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or
    ``action-required``."""

    TWILIO_PROCESSING = "twilio-processing"
    RECEIVED = "received"
    PENDING_VERIFICATION = "pending-verification"
    VERIFIED = "verified"
    PENDING_LOA = "pending-loa"
    CARRIER_PROCESSING = "carrier-processing"
    TESTING = "testing"
    COMPLETED = "completed"
    FAILED = "failed"
    ACTION_REQUIRED = "action-required"

    __str__ = str.__str__


HostedNumberOrderEnumStatusOrStr: TypeAlias = Annotated[
    HostedNumberOrderEnumStatus | str, open_enum_validator(HostedNumberOrderEnumStatus)
]
