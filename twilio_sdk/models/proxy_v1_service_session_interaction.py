from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.interaction_enum_resource_status import InteractionEnumResourceStatusOrStr
from .enums.interaction_enum_type import InteractionEnumTypeOrStr


class ProxyV1ServiceSessionInteraction(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Interaction resource."""

    session_sid: OptionalNullable[str] = UNSET
    """The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Interaction
    resource."""

    data: OptionalNullable[str] = UNSET
    """A JSON string that includes the message body of message interactions (e.g. ``{"body": "hello"}``) or the call
    duration (when available) of a call (e.g. ``{"duration": "5"}``)."""

    type_: Optional[InteractionEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The Type of the Interaction. Can be: ``message``, ``voice`` or ``unknown``."""

    inbound_participant_sid: OptionalNullable[str] = UNSET
    """The SID of the inbound `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ resource."""

    inbound_resource_sid: OptionalNullable[str] = UNSET
    """The SID of the inbound resource; either the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ or
    `Message <https://www.twilio.com/docs/sms/api/message-resource>`__."""

    inbound_resource_status: Optional[InteractionEnumResourceStatusOrStr] = UNSET
    """The inbound resource status of the Interaction. Will always be ``delivered`` for messages and ``in-progress`` for
    calls."""

    inbound_resource_type: OptionalNullable[str] = UNSET
    """The inbound resource type. Can be `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ or `Message
    <https://www.twilio.com/docs/sms/api/message-resource>`__."""

    inbound_resource_url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the Twilio inbound resource"""

    outbound_participant_sid: OptionalNullable[str] = UNSET
    """The SID of the outbound `Participant <https://www.twilio.com/docs/proxy/api/participant>`__)."""

    outbound_resource_sid: OptionalNullable[str] = UNSET
    """The SID of the outbound resource; either the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ or
    `Message <https://www.twilio.com/docs/sms/api/message-resource>`__."""

    outbound_resource_status: Optional[InteractionEnumResourceStatusOrStr] = UNSET
    """The inbound resource status of the Interaction. Will always be ``delivered`` for messages and ``in-progress`` for
    calls."""

    outbound_resource_type: OptionalNullable[str] = UNSET
    """The outbound resource type. Can be: `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ or `Message
    <https://www.twilio.com/docs/sms/api/message-resource>`__."""

    outbound_resource_url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the Twilio outbound resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the Interaction was
    created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Interaction resource."""


class ProxyV1ServiceSessionInteractionDict(TypedDict):
    sid: NotRequired[str | None]
    session_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    data: NotRequired[str | None]
    type_: NotRequired[InteractionEnumTypeOrStr]
    inbound_participant_sid: NotRequired[str | None]
    inbound_resource_sid: NotRequired[str | None]
    inbound_resource_status: NotRequired[InteractionEnumResourceStatusOrStr]
    inbound_resource_type: NotRequired[str | None]
    inbound_resource_url: NotRequired[AnyUrl | None]
    outbound_participant_sid: NotRequired[str | None]
    outbound_resource_sid: NotRequired[str | None]
    outbound_resource_status: NotRequired[InteractionEnumResourceStatusOrStr]
    outbound_resource_type: NotRequired[str | None]
    outbound_resource_url: NotRequired[AnyUrl | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
