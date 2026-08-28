from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebviewSizeType(str, Enum):
    TALL = "TALL"
    FULL = "FULL"
    HALF = "HALF"
    NONE = "NONE"

    __str__ = str.__str__


WebviewSizeTypeOrStr: TypeAlias = Annotated[WebviewSizeType | str, open_enum_validator(WebviewSizeType)]
