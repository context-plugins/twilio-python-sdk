from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaskQueueEnumTaskOrder(str, Enum):
    """How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently created Task first
    or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
    <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more."""

    FIFO = "FIFO"
    LIFO = "LIFO"

    __str__ = str.__str__


TaskQueueEnumTaskOrderOrStr: TypeAlias = Annotated[
    TaskQueueEnumTaskOrder | str, open_enum_validator(TaskQueueEnumTaskOrder)
]
