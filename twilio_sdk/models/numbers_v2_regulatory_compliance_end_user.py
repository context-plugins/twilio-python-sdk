from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.end_user_enum_type import EndUserEnumTypeOrStr


class NumbersV2RegulatoryComplianceEndUser(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify the End User resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the End User resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    type_: Optional[EndUserEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of end user of the Bundle resource - can be ``individual`` or ``business``."""

    attributes: OptionalNullable[Any] = UNSET
    """The set of parameters that are the attributes of the End Users resource which are listed in the End User
    Types."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the End User resource."""


class NumbersV2RegulatoryComplianceEndUserDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    type_: NotRequired[EndUserEnumTypeOrStr]
    attributes: NotRequired[Any | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
