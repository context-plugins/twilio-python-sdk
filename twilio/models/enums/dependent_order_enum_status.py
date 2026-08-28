from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DependentOrderEnumStatus(str, Enum):
    """The status of the hosted number order. Can be: ``twilio-processing``, ``received``, ``pending-verification``,
    ``verified``, ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or
    ``action-required``., Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3.
    Pending LOA, 4. Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders Status
    Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
    section for more information on each of these statuses."""

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


DependentOrderEnumStatusOrStr: TypeAlias = Annotated[
    DependentOrderEnumStatus | str, open_enum_validator(DependentOrderEnumStatus)
]
