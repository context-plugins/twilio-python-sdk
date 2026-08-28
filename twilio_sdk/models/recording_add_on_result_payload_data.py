from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RecordingAddOnResultPayloadData(SdkBaseModel):
    redirect_to: OptionalNullable[AnyUrl] = UNSET
    """The URL to redirect to to get the data returned by the AddOn that was previously stored."""


class RecordingAddOnResultPayloadDataDict(TypedDict):
    redirect_to: NotRequired[AnyUrl | None]
