from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.engagement_enum_status import EngagementEnumStatusOrStr


class StudioV2FlowExecution(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Execution resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Execution resource."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    contact_channel_address: OptionalNullable[str] = UNSET
    """The phone number, SIP address or Client identifier that triggered the Execution. Phone numbers are in E.164
    format (e.g. +16175551212). SIP addresses are formatted as ``name@company.com``. Client identifiers are formatted
    ``client:name``."""

    contact_sid: OptionalNullable[str] = UNSET
    """The SID of the Contact."""

    flow_version: OptionalNullable[int] = UNSET
    """The Flow version number at the time of Execution creation."""

    context: OptionalNullable[Any] = UNSET
    """The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data
    that your widgets can access as variables in configuration fields or in text areas as variable substitution."""

    status: Optional[EngagementEnumStatusOrStr] = UNSET
    """The status of the Execution. Can be: ``active`` or ``ended``."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    initiated_by: OptionalNullable[str] = UNSET
    """The SID or identifier that triggered this Execution. For example, a Call SID if triggered by an incoming call, a
    Message SID if triggered by an incoming message, a Request SID if triggered by a REST API request, and so on."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of nested resources."""


class StudioV2FlowExecutionDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    flow_sid: NotRequired[str | None]
    contact_channel_address: NotRequired[str | None]
    contact_sid: NotRequired[str | None]
    flow_version: NotRequired[int | None]
    context: NotRequired[Any | None]
    status: NotRequired[EngagementEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    initiated_by: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
