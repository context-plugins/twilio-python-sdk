from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV1PortInRequestListMeta(SdkBaseModel):
    previous_token: OptionalNullable[str] = UNSET
    next_token: OptionalNullable[str] = UNSET


class NumbersV1PortInRequestListMetaDict(TypedDict):
    previous_token: NotRequired[str | None]
    next_token: NotRequired[str | None]
