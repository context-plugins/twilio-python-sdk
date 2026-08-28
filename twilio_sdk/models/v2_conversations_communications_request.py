from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .author import Author, AuthorDict
from .recipient2 import Recipient2, Recipient2Dict
from .unions.content2 import Content2, Content2Dict


class V2ConversationsCommunicationsRequest(SdkBaseModel):
    author: Author
    content: Content2
    """The content of the Communication."""

    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")
    recipients: list[Recipient2]


class V2ConversationsCommunicationsRequestDict(TypedDict):
    author: Author | AuthorDict
    content: Content2 | Content2Dict
    channel_id: NotRequired[str]
    recipients: list[Recipient2 | Recipient2Dict]
