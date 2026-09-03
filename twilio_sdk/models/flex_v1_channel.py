from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1Channel(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Channel resource and
    owns this Workflow."""

    flex_flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Flow."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Channel resource."""

    user_sid: OptionalNullable[str] = UNSET
    """The SID of the chat user."""

    task_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskRouter Task. Only valid when integration type is ``task``. ``null`` for integration types
    ``studio`` & ``external``"""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Flex chat channel resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex chat channel was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex chat channel was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""


class FlexV1ChannelDict(TypedDict):
    account_sid: NotRequired[str | None]
    flex_flow_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    user_sid: NotRequired[str | None]
    task_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
