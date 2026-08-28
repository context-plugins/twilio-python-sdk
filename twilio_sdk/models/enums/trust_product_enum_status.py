from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TrustProductEnumStatus(str, Enum):
    """The verification status of the Trust Product resource."""

    DRAFT = "draft"
    PENDING_REVIEW = "pending-review"
    IN_REVIEW = "in-review"
    TWILIO_REJECTED = "twilio-rejected"
    TWILIO_APPROVED = "twilio-approved"

    __str__ = str.__str__


TrustProductEnumStatusOrStr: TypeAlias = Annotated[
    TrustProductEnumStatus | str, open_enum_validator(TrustProductEnumStatus)
]
