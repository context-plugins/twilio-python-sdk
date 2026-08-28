from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkspaceEnumQueueOrder(str, Enum):
    """The type of TaskQueue to prioritize when Workers are receiving Tasks from both types of TaskQueues. Can be:
    ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see `Queue Ordering
    <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__."""

    FIFO = "FIFO"
    LIFO = "LIFO"

    __str__ = str.__str__


WorkspaceEnumQueueOrderOrStr: TypeAlias = Annotated[
    WorkspaceEnumQueueOrder | str, open_enum_validator(WorkspaceEnumQueueOrder)
]
