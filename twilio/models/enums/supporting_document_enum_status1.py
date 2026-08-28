from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SupportingDocumentEnumStatus1(str, Enum):
    """The verification status of the Supporting Document resource."""

    DRAFT = "DRAFT"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    EXPIRED = "EXPIRED"
    PROVISIONALLY_APPROVED = "PROVISIONALLY_APPROVED"

    __str__ = str.__str__


SupportingDocumentEnumStatus1OrStr: TypeAlias = Annotated[
    SupportingDocumentEnumStatus1 | str, open_enum_validator(SupportingDocumentEnumStatus1)
]
