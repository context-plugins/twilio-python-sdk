from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class MessagingV2PresignedUrlResponse(SdkBaseModel):
    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    fetch_url: Optional[str] = Field(default=UNSET, alias="fetchUrl")
    upload_url: Optional[str] = Field(default=UNSET, alias="uploadUrl")
    upload_fields: Optional[Any] = Field(default=UNSET, alias="uploadFields")


class MessagingV2PresignedUrlResponseDict(TypedDict):
    expires_at: NotRequired[RFC3339DateTime]
    fetch_url: NotRequired[str]
    upload_url: NotRequired[str]
    upload_fields: NotRequired[Any]
