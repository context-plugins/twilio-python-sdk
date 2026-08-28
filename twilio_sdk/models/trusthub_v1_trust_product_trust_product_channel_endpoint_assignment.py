from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TrusthubV1TrustProductTrustProductChannelEndpointAssignment(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Item Assignment resource."""

    trust_product_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the CustomerProfile resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Item Assignment
    resource."""

    channel_endpoint_type: OptionalNullable[str] = UNSET
    """The type of channel endpoint. eg: phone-number"""

    channel_endpoint_sid: OptionalNullable[str] = UNSET
    """The SID of an channel endpoint"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Identity resource."""


class TrusthubV1TrustProductTrustProductChannelEndpointAssignmentDict(TypedDict):
    sid: NotRequired[str | None]
    trust_product_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    channel_endpoint_type: NotRequired[str | None]
    channel_endpoint_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
