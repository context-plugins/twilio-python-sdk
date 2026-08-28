from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CarouselActionType(str, Enum):
    URL = "URL"
    PHONE_NUMBER = "PHONE_NUMBER"
    QUICK_REPLY = "QUICK_REPLY"

    __str__ = str.__str__


CarouselActionTypeOrStr: TypeAlias = Annotated[CarouselActionType | str, open_enum_validator(CarouselActionType)]
