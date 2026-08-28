from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountBalance(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    balance: OptionalNullable[str] = UNSET
    """The balance of the Account, in units specified by the unit parameter. Balance changes may not be reflected
    immediately. Child accounts do not contain balance information"""

    currency: OptionalNullable[str] = UNSET
    """The units of currency for the account balance"""


class ApiV2010AccountBalanceDict(TypedDict):
    account_sid: NotRequired[str | None]
    balance: NotRequired[str | None]
    currency: NotRequired[str | None]
