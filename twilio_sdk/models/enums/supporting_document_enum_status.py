from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SupportingDocumentEnumStatus(str, Enum):
    """The verification status of the Supporting Document resource."""

    DRAFT = "draft"
    PENDING_REVIEW = "pending-review"
    REJECTED = "rejected"
    APPROVED = "approved"
    EXPIRED = "expired"
    PROVISIONALLY_APPROVED = "provisionally-approved"

    __str__ = str.__str__


SupportingDocumentEnumStatusOrStr: TypeAlias = Annotated[
    SupportingDocumentEnumStatus | str, open_enum_validator(SupportingDocumentEnumStatus)
]
