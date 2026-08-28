from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SyncV1ServiceSyncStreamStreamMessage(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Stream Message resource."""

    data: OptionalNullable[Any] = UNSET
    """An arbitrary, schema-less object that contains the Stream Message body. Can be up to 4 KiB in length."""


class SyncV1ServiceSyncStreamStreamMessageDict(TypedDict):
    sid: NotRequired[str | None]
    data: NotRequired[Any | None]
