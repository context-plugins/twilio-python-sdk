from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentsEnumBankAccountType(str, Enum):
    """Type of bank account if payment source is ACH. One of ``consumer-checking``, ``consumer-savings``, or
    ``commercial-checking``. The default value is ``consumer-checking``."""

    CONSUMER_CHECKING = "consumer-checking"
    CONSUMER_SAVINGS = "consumer-savings"
    COMMERCIAL_CHECKING = "commercial-checking"

    __str__ = str.__str__


PaymentsEnumBankAccountTypeOrStr: TypeAlias = Annotated[
    PaymentsEnumBankAccountType | str, open_enum_validator(PaymentsEnumBankAccountType)
]
