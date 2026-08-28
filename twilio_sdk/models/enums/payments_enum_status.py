from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentsEnumStatus(str, Enum):
    """Indicates whether the current payment session should be cancelled or completed. When ``cancel`` the payment
    session is cancelled. When ``complete``, Twilio sends the payment information to the selected Pay Connector for
    processing."""

    COMPLETE = "complete"
    CANCEL = "cancel"

    __str__ = str.__str__


PaymentsEnumStatusOrStr: TypeAlias = Annotated[PaymentsEnumStatus | str, open_enum_validator(PaymentsEnumStatus)]
