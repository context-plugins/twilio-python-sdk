from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TrusthubV1TrustProductTrustProductEntityAssignment(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Item Assignment resource."""

    trust_product_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the TrustProduct resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Item Assignment
    resource."""

    object_sid: OptionalNullable[str] = UNSET
    """The SID of an object bag that holds information of the different items."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Identity resource."""


class TrusthubV1TrustProductTrustProductEntityAssignmentDict(TypedDict):
    sid: NotRequired[str | None]
    trust_product_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    object_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
