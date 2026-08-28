from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV1LinkshorteningMessagingServiceDomainAssociation(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain resource."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the messaging service"""

    url: OptionalNullable[str] = UNSET


class MessagingV1LinkshorteningMessagingServiceDomainAssociationDict(TypedDict):
    domain_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    url: NotRequired[str | None]
