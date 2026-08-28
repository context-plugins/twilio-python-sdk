from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewStatus(str, Enum):
    """The new status to set for the port in request."""

    IN_REVIEW = "in_review"
    WAITING_FOR_SIGNATURE = "waiting_for_signature"
    PORT_SUBMITTED = "port_submitted"
    PORT_REJECTED = "port_rejected"
    PORT_PENDING = "port_pending"
    CANCELED = "canceled"
    COMPLETED = "completed"
    CANCELING = "canceling"

    __str__ = str.__str__


NewStatusOrStr: TypeAlias = Annotated[NewStatus | str, open_enum_validator(NewStatus)]
