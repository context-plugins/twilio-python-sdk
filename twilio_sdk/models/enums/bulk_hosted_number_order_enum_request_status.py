from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BulkHostedNumberOrderEnumRequestStatus(str, Enum):
    """A string that shows the status of the current Bulk Hosting request, it can vary between these values:
    'QUEUED','IN_PROGRESS','PROCESSED'"""

    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    PROCESSED = "PROCESSED"

    __str__ = str.__str__


BulkHostedNumberOrderEnumRequestStatusOrStr: TypeAlias = Annotated[
    BulkHostedNumberOrderEnumRequestStatus | str, open_enum_validator(BulkHostedNumberOrderEnumRequestStatus)
]
