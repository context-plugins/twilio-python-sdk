from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State(str, Enum):
    """The state of the application."""

    DRAFT = "DRAFT"
    TWILIO_REVIEW = "TWILIO_REVIEW"
    PENDING_PAYMENT = "PENDING_PAYMENT"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    IN_PROVISIONING = "IN_PROVISIONING"
    PENDING_CARRIER = "PENDING_CARRIER"
    APPROVED = "APPROVED"
    CORRECTIONS_NEEDED = "CORRECTIONS_NEEDED"
    CANCELED = "CANCELED"
    ARCHIVED = "ARCHIVED"

    __str__ = str.__str__


StateOrStr: TypeAlias = Annotated[State | str, open_enum_validator(State)]
