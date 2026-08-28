from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InsightsV1Call(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    url: OptionalNullable[str] = UNSET
    links: OptionalNullable[Any] = UNSET


class InsightsV1CallDict(TypedDict):
    sid: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
