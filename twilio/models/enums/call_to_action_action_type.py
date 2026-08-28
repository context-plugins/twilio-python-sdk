from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallToActionActionType(str, Enum):
    URL = "URL"
    PHONE_NUMBER = "PHONE_NUMBER"
    COPY_CODE = "COPY_CODE"
    VOICE_CALL = "VOICE_CALL"
    VOICE_CALL_REQUEST = "VOICE_CALL_REQUEST"

    __str__ = str.__str__


CallToActionActionTypeOrStr: TypeAlias = Annotated[
    CallToActionActionType | str, open_enum_validator(CallToActionActionType)
]
