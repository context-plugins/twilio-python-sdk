from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1PluginRelease(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Plugin Release resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Plugin Release resource
    and owns this resource."""

    configuration_sid: OptionalNullable[str] = UNSET
    """The SID of the Plugin Configuration resource to release."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Flex Plugin Release was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Plugin Release resource."""


class FlexV1PluginReleaseDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    configuration_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
