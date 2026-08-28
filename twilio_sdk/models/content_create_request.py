from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .types import Types, TypesDict


class ContentCreateRequest(SdkBaseModel):
    """Content creation request body"""

    friendly_name: Optional[str] = UNSET
    """User defined name of the content"""

    variables: Optional[dict[str, str]] = UNSET
    """Key value pairs of variable name to value"""

    language: str
    """Language code for the content"""

    types: Types
    """Content types"""


class ContentCreateRequestDict(TypedDict):
    friendly_name: NotRequired[str]
    variables: NotRequired[dict[str, str]]
    language: str
    types: Types | TypesDict
