from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkerReservationEnumStatus(str, Enum):
    """The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``, ``timeout``,
    ``canceled``, or ``rescinded``."""

    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    TIMEOUT = "timeout"
    CANCELED = "canceled"
    RESCINDED = "rescinded"
    WRAPPING = "wrapping"
    COMPLETED = "completed"

    __str__ = str.__str__


WorkerReservationEnumStatusOrStr: TypeAlias = Annotated[
    WorkerReservationEnumStatus | str, open_enum_validator(WorkerReservationEnumStatus)
]
