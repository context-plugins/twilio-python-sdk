from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class JobThresholds(SdkBaseModel):
    error: OptionalNullable[float] = UNSET


class JobThresholdsDict(TypedDict):
    error: NotRequired[float | None]
