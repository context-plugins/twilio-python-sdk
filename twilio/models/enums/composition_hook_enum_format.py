from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompositionHookEnumFormat(str, Enum):
    """The container format of the media files used by the compositions created by the composition hook. If ``mp4`` or
    ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element must contain a valid
    ``video_sources`` list, otherwise an error occurs."""

    MP4 = "mp4"
    WEBM = "webm"

    __str__ = str.__str__


CompositionHookEnumFormatOrStr: TypeAlias = Annotated[
    CompositionHookEnumFormat | str, open_enum_validator(CompositionHookEnumFormat)
]
