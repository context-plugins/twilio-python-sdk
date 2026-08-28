from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentsEnumTokenType(str, Enum):
    """Indicates whether the payment method should be tokenized as a ``one-time``, ``reusable``, or ``payment-method``
    token. The default value is ``reusable``. Do not enter a charge amount when tokenizing. If a charge amount is
    entered, the payment method will be charged and not tokenized."""

    ONE_TIME = "one-time"
    REUSABLE = "reusable"
    PAYMENT_METHOD = "payment-method"

    __str__ = str.__str__


PaymentsEnumTokenTypeOrStr: TypeAlias = Annotated[
    PaymentsEnumTokenType | str, open_enum_validator(PaymentsEnumTokenType)
]
