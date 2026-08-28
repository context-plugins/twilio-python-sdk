from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompositionEnumFormat(str, Enum):
    """The container format of the composition's media files as specified in the POST request that created the
    Composition resource. See `POST Parameters
    <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more information."""

    MP4 = "mp4"
    WEBM = "webm"

    __str__ = str.__str__


CompositionEnumFormatOrStr: TypeAlias = Annotated[
    CompositionEnumFormat | str, open_enum_validator(CompositionEnumFormat)
]
