from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class ApiV2010AccountUsageUsageRecordUsageRecordToday(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that accrued the usage."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create the resource."""

    as_of: OptionalNullable[str] = UNSET
    """Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in
    GMT"""

    category: OptionalNullable[str] = UNSET
    """The category of usage. For more information, see `Usage Categories
    <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__."""

    count: OptionalNullable[str] = UNSET
    """The number of usage events, such as the number of calls."""

    count_unit: OptionalNullable[str] = UNSET
    """The units in which ``count`` is measured, such as ``calls`` for calls or ``messages`` for SMS."""

    description: OptionalNullable[str] = UNSET
    """A plain-language description of the usage category."""

    end_date: OptionalNullable[Date] = UNSET
    """The last date for which usage is included in the UsageRecord. The date is specified in GMT and formatted as
    ``YYYY-MM-DD``."""

    price: OptionalNullable[float] = UNSET
    """The total price of the usage in the currency specified in ``price_unit`` and associated with the account."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency in which ``price`` is measured, in `ISO 4127
    <https://www.iso.org/iso/home/standards/currency_codes.htm>`__ format, such as ``usd``, ``eur``, and ``jpy``."""

    start_date: OptionalNullable[Date] = UNSET
    """The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as
    ``YYYY-MM-DD``."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their URIs. For more information, see `List Subresources
    <https://www.twilio.com/docs/usage/api/usage-record#list-subresources>`__."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    usage: OptionalNullable[str] = UNSET
    """The amount used to bill usage and measured in units described in ``usage_unit``."""

    usage_unit: OptionalNullable[str] = UNSET
    """The units in which ``usage`` is measured, such as ``minutes`` for calls or ``messages`` for SMS."""


class ApiV2010AccountUsageUsageRecordUsageRecordTodayDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    as_of: NotRequired[str | None]
    category: NotRequired[str | None]
    count: NotRequired[str | None]
    count_unit: NotRequired[str | None]
    description: NotRequired[str | None]
    end_date: NotRequired[Date | None]
    price: NotRequired[float | None]
    price_unit: NotRequired[str | None]
    start_date: NotRequired[Date | None]
    subresource_uris: NotRequired[Any | None]
    uri: NotRequired[str | None]
    usage: NotRequired[str | None]
    usage_unit: NotRequired[str | None]
