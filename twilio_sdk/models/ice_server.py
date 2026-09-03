from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IceServer(SdkBaseModel):
    credential: Optional[str] = UNSET
    username: Optional[str] = UNSET
    url: Optional[str] = UNSET
    urls: Optional[str] = UNSET


class IceServerDict(TypedDict):
    credential: NotRequired[str]
    username: NotRequired[str]
    url: NotRequired[str]
    urls: NotRequired[str]
