from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumCreatedMethod(str, Enum):
    SDK = "sdk"
    AD_HOC = "ad_hoc"
    API = "api"

    __str__ = str.__str__


VideoRoomSummaryEnumCreatedMethodOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumCreatedMethod | str, open_enum_validator(VideoRoomSummaryEnumCreatedMethod)
]
