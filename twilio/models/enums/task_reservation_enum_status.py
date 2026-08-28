from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaskReservationEnumStatus(str, Enum):
    """The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``, or ``timeout``."""

    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    TIMEOUT = "timeout"
    CANCELED = "canceled"
    RESCINDED = "rescinded"
    WRAPPING = "wrapping"
    COMPLETED = "completed"

    __str__ = str.__str__


TaskReservationEnumStatusOrStr: TypeAlias = Annotated[
    TaskReservationEnumStatus | str, open_enum_validator(TaskReservationEnumStatus)
]
