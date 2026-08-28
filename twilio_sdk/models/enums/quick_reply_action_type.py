from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QuickReplyActionType(str, Enum):
    QUICK_REPLY = "QUICK_REPLY"

    __str__ = str.__str__


QuickReplyActionTypeOrStr: TypeAlias = Annotated[QuickReplyActionType | str, open_enum_validator(QuickReplyActionType)]
