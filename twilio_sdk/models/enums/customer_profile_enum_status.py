from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerProfileEnumStatus(str, Enum):
    """The verification status of the Customer-Profile resource."""

    DRAFT = "draft"
    PENDING_REVIEW = "pending-review"
    IN_REVIEW = "in-review"
    TWILIO_REJECTED = "twilio-rejected"
    TWILIO_APPROVED = "twilio-approved"

    __str__ = str.__str__


CustomerProfileEnumStatusOrStr: TypeAlias = Annotated[
    CustomerProfileEnumStatus | str, open_enum_validator(CustomerProfileEnumStatus)
]
