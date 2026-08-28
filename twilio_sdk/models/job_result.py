from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class JobResult(SdkBaseModel):
    file_url: OptionalNullable[AnyUrl] = UNSET
    total_count: Optional[int] = UNSET
    processed_count: Optional[int] = UNSET
    success_count: Optional[int] = UNSET
    error_count: Optional[int] = UNSET
    details: OptionalNullable[str] = UNSET


class JobResultDict(TypedDict):
    file_url: NotRequired[AnyUrl | None]
    total_count: NotRequired[int]
    processed_count: NotRequired[int]
    success_count: NotRequired[int]
    error_count: NotRequired[int]
    details: NotRequired[str | None]
