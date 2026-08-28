from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.message_interaction_enum_resource_status import MessageInteractionEnumResourceStatusOrStr
from .enums.message_interaction_enum_type import MessageInteractionEnumTypeOrStr


class ProxyV1ServiceSessionParticipantMessageInteraction(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the MessageInteraction resource."""

    session_sid: OptionalNullable[str] = UNSET
    """The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the MessageInteraction
    resource."""

    data: OptionalNullable[str] = UNSET
    """A JSON string that includes the message body sent to the participant. (e.g. ``{"body": "hello"}``)"""

    type_: Optional[MessageInteractionEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The Type of Message Interaction. This value is always ``message``."""

    participant_sid: OptionalNullable[str] = UNSET
    """The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ resource."""

    inbound_participant_sid: OptionalNullable[str] = UNSET
    """Always empty for created Message Interactions."""

    inbound_resource_sid: OptionalNullable[str] = UNSET
    """Always empty for created Message Interactions."""

    inbound_resource_status: Optional[MessageInteractionEnumResourceStatusOrStr] = UNSET
    """Always empty for created Message Interactions."""

    inbound_resource_type: OptionalNullable[str] = UNSET
    """Always empty for created Message Interactions."""

    inbound_resource_url: OptionalNullable[str] = UNSET
    """Always empty for created Message Interactions."""

    outbound_participant_sid: OptionalNullable[str] = UNSET
    """The SID of the outbound `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ resource."""

    outbound_resource_sid: OptionalNullable[str] = UNSET
    """The SID of the outbound `Message <https://www.twilio.com/docs/sms/api/message-resource>`__ resource."""

    outbound_resource_status: Optional[MessageInteractionEnumResourceStatusOrStr] = UNSET
    """Always empty for created Message Interactions."""

    outbound_resource_type: OptionalNullable[str] = UNSET
    """The outbound resource type. This value is always ``Message``."""

    outbound_resource_url: OptionalNullable[str] = UNSET
    """The URL of the Twilio message resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the MessageInteraction resource."""


class ProxyV1ServiceSessionParticipantMessageInteractionDict(TypedDict):
    sid: NotRequired[str | None]
    session_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    data: NotRequired[str | None]
    type_: NotRequired[MessageInteractionEnumTypeOrStr]
    participant_sid: NotRequired[str | None]
    inbound_participant_sid: NotRequired[str | None]
    inbound_resource_sid: NotRequired[str | None]
    inbound_resource_status: NotRequired[MessageInteractionEnumResourceStatusOrStr]
    inbound_resource_type: NotRequired[str | None]
    inbound_resource_url: NotRequired[str | None]
    outbound_participant_sid: NotRequired[str | None]
    outbound_resource_sid: NotRequired[str | None]
    outbound_resource_status: NotRequired[MessageInteractionEnumResourceStatusOrStr]
    outbound_resource_type: NotRequired[str | None]
    outbound_resource_url: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
