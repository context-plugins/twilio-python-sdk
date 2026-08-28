from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.engagement_enum_status import EngagementEnumStatusOrStr


class StudioV1FlowEngagement(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Engagement resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Engagement resource."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    contact_sid: OptionalNullable[str] = UNSET
    """The SID of the Contact."""

    contact_channel_address: OptionalNullable[str] = UNSET
    """The phone number, SIP address or Client identifier that triggered this Engagement. Phone numbers are in E.164
    format (+16175551212). SIP addresses are formatted as ``name@company.com``. Client identifiers are formatted
    ``client:name``."""

    context: OptionalNullable[Any] = UNSET
    """The current state of the execution flow. As your flow executes, we save the state in a flow context. Your widgets
    can access the data in the flow context as variables, either in configuration fields or in text areas as variable
    substitution."""

    status: Optional[EngagementEnumStatusOrStr] = UNSET
    """The status of the Engagement. Can be: ``active`` or ``ended``."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Engagement was created in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Engagement was updated in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Engagement's nested resources."""


class StudioV1FlowEngagementDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    flow_sid: NotRequired[str | None]
    contact_sid: NotRequired[str | None]
    contact_channel_address: NotRequired[str | None]
    context: NotRequired[Any | None]
    status: NotRequired[EngagementEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
