from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1PluginConfigurationConfiguredPlugin(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that the Flex Plugin resource is
    installed for."""

    configuration_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Plugin Configuration that this Flex Plugin belongs to."""

    plugin_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Plugin."""

    plugin_version_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex Plugin Version."""

    phase: Optional[int] = UNSET
    """The phase this Flex Plugin would initialize at runtime."""

    plugin_url: OptionalNullable[str] = UNSET
    """The URL of where the Flex Plugin Version JavaScript bundle is hosted on."""

    unique_name: OptionalNullable[str] = UNSET
    """The name that uniquely identifies this Flex Plugin resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The friendly name of this Flex Plugin resource."""

    description: OptionalNullable[str] = UNSET
    """A descriptive string that you create to describe the plugin resource. It can be up to 500 characters long"""

    plugin_archived: OptionalNullable[bool] = UNSET
    """Whether the Flex Plugin is archived. The default value is false."""

    version: OptionalNullable[str] = UNSET
    """The latest version of this Flex Plugin Version."""

    changelog: OptionalNullable[str] = UNSET
    """A changelog that describes the changes this Flex Plugin Version brings."""

    plugin_version_archived: OptionalNullable[bool] = UNSET
    """Whether the Flex Plugin Version is archived. The default value is false."""

    private: OptionalNullable[bool] = UNSET
    """Whether to validate the request is authorized to access the Flex Plugin Version."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin was installed specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Flex Plugin resource."""


class FlexV1PluginConfigurationConfiguredPluginDict(TypedDict):
    account_sid: NotRequired[str | None]
    configuration_sid: NotRequired[str | None]
    plugin_sid: NotRequired[str | None]
    plugin_version_sid: NotRequired[str | None]
    phase: NotRequired[int]
    plugin_url: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    description: NotRequired[str | None]
    plugin_archived: NotRequired[bool | None]
    version: NotRequired[str | None]
    changelog: NotRequired[str | None]
    plugin_version_archived: NotRequired[bool | None]
    private: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
