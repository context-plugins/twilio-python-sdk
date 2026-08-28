from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountSigningKey(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    friendly_name: OptionalNullable[str] = UNSET
    date_created: OptionalNullable[str] = UNSET
    date_updated: OptionalNullable[str] = UNSET


class ApiV2010AccountSigningKeyDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
