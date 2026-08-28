from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.event_enum_level import EventEnumLevelOrStr
from .enums.event_enum_twilio_edge import EventEnumTwilioEdgeOrStr


class InsightsV1CallEvent(SdkBaseModel):
    timestamp: OptionalNullable[str] = UNSET
    """Event time."""

    call_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Call."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    edge: Optional[EventEnumTwilioEdgeOrStr] = UNSET
    group: OptionalNullable[str] = UNSET
    """Event group."""

    level: Optional[EventEnumLevelOrStr] = UNSET
    name: OptionalNullable[str] = UNSET
    """Event name."""

    carrier_edge: OptionalNullable[Any] = UNSET
    """``object`` Represents the connection between Twilio and our immediate carrier partners. The events here describe
    the call lifecycle as reported by Twilio's carrier media gateways. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    sip_edge: OptionalNullable[Any] = UNSET
    """``object`` Represents the Twilio media gateway for SIP interface and SIP trunking calls. The events here describe
    the call lifecycle as reported by Twilio's public media gateways. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    sdk_edge: OptionalNullable[Any] = UNSET
    """``object`` Represents the Voice SDK running locally in the browser or in the Android/iOS application. The events
    here are emitted by the Voice SDK in response to certain call progress events, network changes, or call quality
    conditions. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""

    client_edge: OptionalNullable[Any] = UNSET
    """``object`` Represents the Twilio media gateway for Client calls. The events here describe the call lifecycle as
    reported by Twilio's Voice SDK media gateways. See `Details: Call Summary
    <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-summary#edges-and-their-properties>`__ for
    the object properties."""


class InsightsV1CallEventDict(TypedDict):
    timestamp: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    edge: NotRequired[EventEnumTwilioEdgeOrStr]
    group: NotRequired[str | None]
    level: NotRequired[EventEnumLevelOrStr]
    name: NotRequired[str | None]
    carrier_edge: NotRequired[Any | None]
    sip_edge: NotRequired[Any | None]
    sdk_edge: NotRequired[Any | None]
    client_edge: NotRequired[Any | None]
