from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1PluginVersionArchive(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flex Plugin Version resource."""

    plugin_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Plugin resource this Flex Plugin Version belongs to."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Plugin Version
    resource and owns this resource."""

    version: OptionalNullable[str] = UNSET
    """The unique version of this Flex Plugin Version."""

    plugin_url: OptionalNullable[str] = UNSET
    """The URL of where the Flex Plugin Version JavaScript bundle is hosted on."""

    changelog: OptionalNullable[str] = UNSET
    """A changelog that describes the changes this Flex Plugin Version brings."""

    private: OptionalNullable[bool] = UNSET
    """Whether to inject credentials while accessing this Plugin Version. The default value is false."""

    archived: OptionalNullable[bool] = UNSET
    """Whether the Flex Plugin Version is archived. The default value is false."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin Version was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Flex Plugin Version resource."""


class FlexV1PluginVersionArchiveDict(TypedDict):
    sid: NotRequired[str | None]
    plugin_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    version: NotRequired[str | None]
    plugin_url: NotRequired[str | None]
    changelog: NotRequired[str | None]
    private: NotRequired[bool | None]
    archived: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
