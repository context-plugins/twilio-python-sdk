from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class OptOutConfig(SdkBaseModel):
    opt_out_sid: str
    """The unique SID identifier for the opt-out configuration"""

    account_sid: str
    """The SID of the account that owns this opt-out configuration"""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable name for the opt-out configuration"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time when the opt-out configuration was created"""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time when the opt-out configuration was last updated"""


class OptOutConfigDict(TypedDict):
    opt_out_sid: str
    account_sid: str
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
