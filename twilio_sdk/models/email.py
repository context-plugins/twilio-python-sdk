from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Email(SdkBaseModel):
    email: Optional[str] = UNSET
    label: Optional[str] = UNSET


class EmailDict(TypedDict):
    email: NotRequired[str]
    label: NotRequired[str]
