from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .types import Types, TypesDict


class ContentUpdateRequest(SdkBaseModel):
    """Content update request body"""

    friendly_name: Optional[str] = UNSET
    """User defined name of the content"""

    variables: Optional[dict[str, str]] = UNSET
    """Key value pairs of variable name to value"""

    language: Optional[str] = UNSET
    """Language code for the content"""

    types: Types
    """Content types"""


class ContentUpdateRequestDict(TypedDict):
    friendly_name: NotRequired[str]
    variables: NotRequired[dict[str, str]]
    language: NotRequired[str]
    types: Types | TypesDict
