from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentsEnumPaymentMethod(str, Enum):
    """Type of payment being captured. One of ``credit-card`` or ``ach-debit``. The default value is ``credit-card``."""

    CREDIT_CARD = "credit-card"
    ACH_DEBIT = "ach-debit"

    __str__ = str.__str__


PaymentsEnumPaymentMethodOrStr: TypeAlias = Annotated[
    PaymentsEnumPaymentMethod | str, open_enum_validator(PaymentsEnumPaymentMethod)
]
