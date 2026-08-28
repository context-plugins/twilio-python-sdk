from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sdk import Sdk, SdkDict
from .twilio_gateway import TwilioGateway, TwilioGatewayDict


class NetworkIssues(SdkBaseModel):
    """Network-quality indicators for SDK and Twilio Gateway traffic during the report period."""

    sdk: Optional[Sdk] = UNSET
    """Network issues of calls for client type. This is indicative of local network issues."""

    twilio_gateway: Optional[TwilioGateway] = UNSET
    """Network related metrics for Twilio Gateway calls only."""


class NetworkIssuesDict(TypedDict):
    sdk: NotRequired[Sdk | SdkDict]
    twilio_gateway: NotRequired[TwilioGateway | TwilioGatewayDict]
