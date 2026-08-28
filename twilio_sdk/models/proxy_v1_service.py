from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.service_enum_geo_match_level import ServiceEnumGeoMatchLevelOrStr
from .enums.service_enum_number_selection_behavior import ServiceEnumNumberSelectionBehaviorOrStr


class ProxyV1Service(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Service resource."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer
    in length and be unique. Supports UTF-8 characters. **This value should not have PII.**"""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    chat_instance_sid: OptionalNullable[str] = UNSET
    """The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and
    channel messages to this chat instance. This is a one-to-one relationship."""

    callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when the interaction status changes."""

    default_ttl: Optional[int] = UNSET
    """The default ``ttl`` value for Sessions created in the Service. The TTL (time to live) is measured in seconds
    after the Session's last create or last Interaction. The default value of ``0`` indicates an unlimited Session
    length. You can override a Session's default TTL value by setting its ``ttl`` value."""

    number_selection_behavior: Optional[ServiceEnumNumberSelectionBehaviorOrStr] = UNSET
    """The preference for Proxy Number selection in the Service instance. Can be: ``prefer-sticky`` or ``avoid-sticky``.
    ``prefer-sticky`` means that we will try and select the same Proxy Number for a given participant if they have
    previous `Sessions <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number
    cannot be used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
    within a given pool rather than try and use a previously assigned number."""

    geo_match_level: Optional[ServiceEnumGeoMatchLevelOrStr] = UNSET
    """Where a proxy number must be located relative to the participant identifier. Can be: ``country``, ``area-code``,
    or ``extended-area-code``. The default value is ``country`` and more specific areas than ``country`` are only
    available in North America."""

    intercept_callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the
    interaction continues."""

    out_of_session_callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or
    a Twilio `function <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
    <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for example, to play a
    message for a call, send an automated text message response, or redirect a call to another Phone Number. See
    `Out-of-Session Callback Response Guide <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__
    for more information."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Service resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of resources related to the Service."""


class ProxyV1ServiceDict(TypedDict):
    sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    chat_instance_sid: NotRequired[str | None]
    callback_url: NotRequired[AnyUrl | None]
    default_ttl: NotRequired[int]
    number_selection_behavior: NotRequired[ServiceEnumNumberSelectionBehaviorOrStr]
    geo_match_level: NotRequired[ServiceEnumGeoMatchLevelOrStr]
    intercept_callback_url: NotRequired[AnyUrl | None]
    out_of_session_callback_url: NotRequired[AnyUrl | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
