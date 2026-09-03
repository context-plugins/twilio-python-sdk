from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RecordingAddOnResultPayloadData(SdkBaseModel):
    redirect_to: OptionalNullable[str] = UNSET
    """The URL to redirect to to get the data returned by the AddOn that was previously stored."""


class RecordingAddOnResultPayloadDataDict(TypedDict):
    redirect_to: NotRequired[str | None]
