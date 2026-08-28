from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DependentHostedNumberOrderEnumStatus(str, Enum):
    """Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled,
    5. failed. See the section entitled `Status Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
    for more information on each of these statuses."""

    RECEIVED = "received"
    VERIFIED = "verified"
    PENDING_LOA = "pending-loa"
    CARRIER_PROCESSING = "carrier-processing"
    COMPLETED = "completed"
    FAILED = "failed"
    ACTION_REQUIRED = "action-required"

    __str__ = str.__str__


DependentHostedNumberOrderEnumStatusOrStr: TypeAlias = Annotated[
    DependentHostedNumberOrderEnumStatus | str, open_enum_validator(DependentHostedNumberOrderEnumStatus)
]
