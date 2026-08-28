from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BundleCopyEnumStatus(str, Enum):
    """The verification status of the Bundle resource."""

    DRAFT = "draft"
    PENDING_REVIEW = "pending-review"
    IN_REVIEW = "in-review"
    TWILIO_REJECTED = "twilio-rejected"
    TWILIO_APPROVED = "twilio-approved"
    PROVISIONALLY_APPROVED = "provisionally-approved"

    __str__ = str.__str__


BundleCopyEnumStatusOrStr: TypeAlias = Annotated[BundleCopyEnumStatus | str, open_enum_validator(BundleCopyEnumStatus)]
