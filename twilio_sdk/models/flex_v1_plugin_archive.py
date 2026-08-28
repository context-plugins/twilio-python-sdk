from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1PluginArchive(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flex Plugin resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Plugin resource
    and owns this resource."""

    unique_name: OptionalNullable[str] = UNSET
    """The name that uniquely identifies this Flex Plugin resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The friendly name this Flex Plugin resource."""

    description: OptionalNullable[str] = UNSET
    """A descriptive string that you create to describe the plugin resource. It can be up to 500 characters long"""

    archived: OptionalNullable[bool] = UNSET
    """Whether the Flex Plugin is archived. The default value is false."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Flex Plugin resource."""


class FlexV1PluginArchiveDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    description: NotRequired[str | None]
    archived: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
