from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlowEnumStatus(str, Enum):
    """The status of the Flow. Can be: ``draft`` or ``published``."""

    DRAFT = "draft"
    PUBLISHED = "published"

    __str__ = str.__str__


FlowEnumStatusOrStr: TypeAlias = Annotated[FlowEnumStatus | str, open_enum_validator(FlowEnumStatus)]
