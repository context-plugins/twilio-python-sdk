from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsV2SendMessageContent(SdkBaseModel):
    """Content for a SEND_MESSAGE action."""

    text: Optional[str] = UNSET
    """Plain text message body."""

    content_id: Optional[str] = Field(default=UNSET, alias="contentId")
    """Content template ID (HX... format). When provided, the template is rendered with the variables map and sent to
    the recipient."""

    variables: Optional[dict[str, str]] = UNSET
    """Variables to substitute into the content template."""

    media_urls: Optional[list[str]] = Field(default=UNSET, alias="mediaUrls")
    """URLs of media attachments to include with the message."""


class ConversationsV2SendMessageContentDict(TypedDict):
    text: NotRequired[str]
    content_id: NotRequired[str]
    variables: NotRequired[dict[str, str]]
    media_urls: NotRequired[list[str]]
