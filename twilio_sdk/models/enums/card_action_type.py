from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardActionType(str, Enum):
    URL = "URL"
    PHONE_NUMBER = "PHONE_NUMBER"
    QUICK_REPLY = "QUICK_REPLY"
    COPY_CODE = "COPY_CODE"
    VOICE_CALL = "VOICE_CALL"

    __str__ = str.__str__


CardActionTypeOrStr: TypeAlias = Annotated[CardActionType | str, open_enum_validator(CardActionType)]
