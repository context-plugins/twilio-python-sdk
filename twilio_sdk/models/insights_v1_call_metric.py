from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.metric_enum_stream_direction import MetricEnumStreamDirectionOrStr
from .enums.metric_enum_twilio_edge import MetricEnumTwilioEdgeOrStr


class InsightsV1CallMetric(SdkBaseModel):
    timestamp: OptionalNullable[str] = UNSET
    """Timestamp of metric sample. Samples are taken every 10 seconds and contain the metrics for the previous 10
    seconds."""

    call_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Call."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    edge: Optional[MetricEnumTwilioEdgeOrStr] = UNSET
    direction: Optional[MetricEnumStreamDirectionOrStr] = UNSET
    carrier_edge: OptionalNullable[Any] = UNSET
    """Contains metrics and properties for the Twilio media gateway of a PSTN call."""

    sip_edge: OptionalNullable[Any] = UNSET
    """Contains metrics and properties for the Twilio media gateway of a SIP Interface or Trunking call."""

    sdk_edge: OptionalNullable[Any] = UNSET
    """Contains metrics and properties for the SDK sensor library for Client calls."""

    client_edge: OptionalNullable[Any] = UNSET
    """Contains metrics and properties for the Twilio media gateway of a Client call."""


class InsightsV1CallMetricDict(TypedDict):
    timestamp: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    edge: NotRequired[MetricEnumTwilioEdgeOrStr]
    direction: NotRequired[MetricEnumStreamDirectionOrStr]
    carrier_edge: NotRequired[Any | None]
    sip_edge: NotRequired[Any | None]
    sdk_edge: NotRequired[Any | None]
    client_edge: NotRequired[Any | None]
