from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportStatus(str, Enum):
    """The status of the report."""

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"

    __str__ = str.__str__


ReportStatusOrStr: TypeAlias = Annotated[ReportStatus | str, open_enum_validator(ReportStatus)]
