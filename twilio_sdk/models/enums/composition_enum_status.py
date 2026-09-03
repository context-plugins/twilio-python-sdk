from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompositionEnumStatus(str, Enum):
    """The status of the composition. Can be: ``enqueued``, ``processing``, ``completed``, ``deleted`` or ``failed``.
    ``enqueued`` is the initial state and indicates that the composition request has been received and is scheduled for
    processing; ``processing`` indicates the composition is being processed; ``completed`` indicates the composition has
    been completed and is available for download; ``deleted`` means the composition media has been deleted from the
    system, but its metadata is still available for 30 days; ``failed`` indicates the composition failed to execute the
    media processing task."""

    ENQUEUED = "enqueued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    DELETED = "deleted"
    FAILED = "failed"

    __str__ = str.__str__


CompositionEnumStatusOrStr: TypeAlias = Annotated[
    CompositionEnumStatus | str, open_enum_validator(CompositionEnumStatus)
]
