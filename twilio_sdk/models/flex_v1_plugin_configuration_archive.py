from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1PluginConfigurationArchive(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flex Plugin Configuration resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Plugin
    Configuration resource and owns this resource."""

    name: OptionalNullable[str] = UNSET
    """The name of this Flex Plugin Configuration."""

    description: OptionalNullable[str] = UNSET
    """The description of the Flex Plugin Configuration resource."""

    archived: OptionalNullable[bool] = UNSET
    """Whether the Flex Plugin Configuration is archived. The default value is false."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin Configuration was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Flex Plugin Configuration resource."""


class FlexV1PluginConfigurationArchiveDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    archived: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
