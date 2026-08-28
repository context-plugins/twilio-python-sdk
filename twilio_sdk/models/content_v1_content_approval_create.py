from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ContentV1ContentApprovalCreate(SdkBaseModel):
    name: OptionalNullable[str] = UNSET
    category: OptionalNullable[str] = UNSET
    content_type: OptionalNullable[str] = UNSET
    status: OptionalNullable[str] = UNSET
    rejection_reason: OptionalNullable[str] = UNSET
    allow_category_change: OptionalNullable[bool] = UNSET


class ContentV1ContentApprovalCreateDict(TypedDict):
    name: NotRequired[str | None]
    category: NotRequired[str | None]
    content_type: NotRequired[str | None]
    status: NotRequired[str | None]
    rejection_reason: NotRequired[str | None]
    allow_category_change: NotRequired[bool | None]
