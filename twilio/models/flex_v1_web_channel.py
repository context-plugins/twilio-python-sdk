from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1WebChannel(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the WebChannel resource and
    owns this Workflow."""

    flex_flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Flow."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the WebChannel resource."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the WebChannel resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""


class FlexV1WebChannelDict(TypedDict):
    account_sid: NotRequired[str | None]
    flex_flow_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    url: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
