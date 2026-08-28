from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BrandRegistrationsEnumStatus(str, Enum):
    """Brand Registration status. One of "PENDING", "APPROVED", "FAILED", "IN_REVIEW", "DELETION_PENDING",
    "DELETION_FAILED", "SUSPENDED"."""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    IN_REVIEW = "IN_REVIEW"
    DELETION_PENDING = "DELETION_PENDING"
    DELETION_FAILED = "DELETION_FAILED"
    SUSPENDED = "SUSPENDED"

    __str__ = str.__str__


BrandRegistrationsEnumStatusOrStr: TypeAlias = Annotated[
    BrandRegistrationsEnumStatus | str, open_enum_validator(BrandRegistrationsEnumStatus)
]
