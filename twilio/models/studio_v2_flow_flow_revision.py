from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.flow_enum_status import FlowEnumStatusOrStr


class StudioV2FlowFlowRevision(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flow resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flow resource."""

    author_sid: OptionalNullable[str] = UNSET
    """The SID of the User that created or last updated the Flow."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the Flow."""

    definition: OptionalNullable[Any] = UNSET
    """JSON representation of flow definition."""

    status: Optional[FlowEnumStatusOrStr] = UNSET
    """The status of the Flow. Can be: ``draft`` or ``published``."""

    revision: Optional[int] = UNSET
    """The latest revision number of the Flow's definition."""

    commit_message: OptionalNullable[str] = UNSET
    """Description of change made in the revision."""

    valid: OptionalNullable[bool] = UNSET
    """Boolean if the flow definition is valid."""

    errors: Optional[list[Any | None]] = UNSET
    """List of error in the flow definition."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""


class StudioV2FlowFlowRevisionDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    author_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    definition: NotRequired[Any | None]
    status: NotRequired[FlowEnumStatusOrStr]
    revision: NotRequired[int]
    commit_message: NotRequired[str | None]
    valid: NotRequired[bool | None]
    errors: NotRequired[list[Any | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
