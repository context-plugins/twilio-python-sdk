from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.bulk_hosted_number_order_enum_request_status import BulkHostedNumberOrderEnumRequestStatusOrStr


class NumbersV2BulkHostedNumberOrder(SdkBaseModel):
    bulk_hosting_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this BulkHostedNumberOrder."""

    request_status: Optional[BulkHostedNumberOrderEnumRequestStatusOrStr] = UNSET
    """A string that shows the status of the current Bulk Hosting request, it can vary between these values:
    'QUEUED','IN_PROGRESS','PROCESSED'"""

    friendly_name: OptionalNullable[str] = UNSET
    """A 128 character string that is a human-readable text that describes this resource."""

    notification_email: OptionalNullable[str] = UNSET
    """Email address used for send notifications about this Bulk hosted number request."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date this resource was created, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_completed: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was completed, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__
    format."""

    url: OptionalNullable[str] = UNSET
    """The URL of this BulkHostedNumberOrder resource."""

    total_count: Optional[int] = UNSET
    """The total count of phone numbers in this Bulk hosting request."""

    results: Optional[list[Any | None]] = UNSET
    """Contains a list of all the individual hosting orders and their information, for this Bulk request. Each result
    object is grouped by its order status. To see a complete list of order status, please check
    'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'."""


class NumbersV2BulkHostedNumberOrderDict(TypedDict):
    bulk_hosting_sid: NotRequired[str | None]
    request_status: NotRequired[BulkHostedNumberOrderEnumRequestStatusOrStr]
    friendly_name: NotRequired[str | None]
    notification_email: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_completed: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    total_count: NotRequired[int]
    results: NotRequired[list[Any | None]]
