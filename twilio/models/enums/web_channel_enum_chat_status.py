from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebChannelEnumChatStatus(str, Enum):
    INACTIVE = "inactive"

    __str__ = str.__str__


WebChannelEnumChatStatusOrStr: TypeAlias = Annotated[
    WebChannelEnumChatStatus | str, open_enum_validator(WebChannelEnumChatStatus)
]
