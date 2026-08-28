from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Billing(SdkBaseModel):
    """The billing information for the phone number."""

    recurring_billable_item_sid: Optional[str] = Field(default=UNSET, alias="RecurringBillableItemSid")
    setup_billable_item_sid: Optional[str] = Field(default=UNSET, alias="SetupBillableItemSid")


class BillingDict(TypedDict):
    recurring_billable_item_sid: NotRequired[str]
    setup_billable_item_sid: NotRequired[str]
