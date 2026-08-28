from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3InsightsDomainsConversationsMetadata500Error1(SdkBaseModel):
    code: int
    """Twilio-specific error code"""

    message: str
    """A human readable error message"""

    http_status_code: int = Field(alias="httpStatusCode")
    """HTTP response status code"""

    user_error: Optional[bool] = Field(default=UNSET, alias="userError")
    """Whether the error is a user error (true) or a system error (false)"""

    params: Optional[dict[str, str]] = UNSET
    """A map of parameters related to the error, for example, a ``params.twilioErrorCodeUrl`` might hold a URL or link
    to additional information"""


class V3InsightsDomainsConversationsMetadata500Error1Dict(TypedDict):
    code: int
    message: str
    http_status_code: int
    user_error: NotRequired[bool]
    params: NotRequired[dict[str, str]]
