from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.flow_enum_status import FlowEnumStatusOrStr


class StudioV1Flow(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flow resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flow resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the Flow."""

    status: Optional[FlowEnumStatusOrStr] = UNSET
    """The status of the Flow. Can be: ``draft`` or ``published``."""

    version: Optional[int] = UNSET
    """The latest version number of the Flow's definition."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Flow's nested resources."""


class StudioV1FlowDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[FlowEnumStatusOrStr]
    version: NotRequired[int]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
