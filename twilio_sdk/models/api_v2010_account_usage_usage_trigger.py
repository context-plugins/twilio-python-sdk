from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.callback_method import CallbackMethodOrStr
from .enums.usage_trigger_enum_recurring import UsageTriggerEnumRecurringOrStr
from .enums.usage_trigger_enum_trigger_field import UsageTriggerEnumTriggerFieldOrStr


class ApiV2010AccountUsageUsageTrigger(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that the trigger monitors."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create the resource."""

    callback_method: OptionalNullable[CallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``callback_url``. Can be: ``GET`` or ``POST``."""

    callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using the ``callback_method`` when the trigger fires."""

    current_value: OptionalNullable[str] = UNSET
    """The current value of the field the trigger is watching."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_fired: OptionalNullable[str] = UNSET
    """The date and time in GMT that the trigger was last fired specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the trigger."""

    recurring: Optional[UsageTriggerEnumRecurringOrStr] = UNSET
    """The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for recurring triggers
    or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in
    GMT."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the UsageTrigger resource."""

    trigger_by: Optional[UsageTriggerEnumTriggerFieldOrStr] = UNSET
    """The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource that fires the
    trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords documentation
    <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__."""

    trigger_value: OptionalNullable[str] = UNSET
    """The value at which the trigger will fire. Must be a positive, numeric value."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    usage_category: OptionalNullable[str] = UNSET
    """The usage category the trigger watches. Must be one of the supported `usage categories
    <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__."""

    usage_record_uri: OptionalNullable[str] = UNSET
    """The URI of the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource this trigger
    watches, relative to ``https://api.twilio.com``."""


class ApiV2010AccountUsageUsageTriggerDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    callback_method: NotRequired[CallbackMethodOrStr | None]
    callback_url: NotRequired[AnyUrl | None]
    current_value: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_fired: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    recurring: NotRequired[UsageTriggerEnumRecurringOrStr]
    sid: NotRequired[str | None]
    trigger_by: NotRequired[UsageTriggerEnumTriggerFieldOrStr]
    trigger_value: NotRequired[str | None]
    uri: NotRequired[str | None]
    usage_category: NotRequired[str | None]
    usage_record_uri: NotRequired[str | None]
