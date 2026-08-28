from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumStatus(str, Enum):
    """The compliance status of the Tollfree Verification record."""

    PENDING_REVIEW = "PENDING_REVIEW"
    IN_REVIEW = "IN_REVIEW"
    TWILIO_APPROVED = "TWILIO_APPROVED"
    TWILIO_REJECTED = "TWILIO_REJECTED"

    __str__ = str.__str__


TollfreeVerificationEnumStatusOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumStatus | str, open_enum_validator(TollfreeVerificationEnumStatus)
]
