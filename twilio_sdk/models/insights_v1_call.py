from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InsightsV1Call(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET
    links: OptionalNullable[Any] = UNSET


class InsightsV1CallDict(TypedDict):
    sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
