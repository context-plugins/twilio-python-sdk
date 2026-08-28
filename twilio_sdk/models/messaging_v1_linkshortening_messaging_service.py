from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV1LinkshorteningMessagingService(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string identifies the domain resource"""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the messaging service"""

    url: OptionalNullable[AnyUrl] = UNSET


class MessagingV1LinkshorteningMessagingServiceDict(TypedDict):
    domain_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
