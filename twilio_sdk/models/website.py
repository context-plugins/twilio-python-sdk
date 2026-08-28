from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Website(SdkBaseModel):
    website: Optional[str] = UNSET
    label: Optional[str] = UNSET


class WebsiteDict(TypedDict):
    website: NotRequired[str]
    label: NotRequired[str]
