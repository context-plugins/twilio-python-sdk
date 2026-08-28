from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentsEnumCapture(str, Enum):
    """The piece of payment information that you wish the caller to enter. Must be one of ``payment-card-number``,
    ``expiration-date``, ``security-code``, ``postal-code``, ``bank-routing-number``, ``bank-account-number``, or their
    ``-matcher`` variants for input confirmation when ``RequireMatchingInputs`` is enabled."""

    PAYMENT_CARD_NUMBER = "payment-card-number"
    EXPIRATION_DATE = "expiration-date"
    SECURITY_CODE = "security-code"
    POSTAL_CODE = "postal-code"
    BANK_ROUTING_NUMBER = "bank-routing-number"
    BANK_ACCOUNT_NUMBER = "bank-account-number"
    PAYMENT_CARD_NUMBER_MATCHER = "payment-card-number-matcher"
    EXPIRATION_DATE_MATCHER = "expiration-date-matcher"
    SECURITY_CODE_MATCHER = "security-code-matcher"
    POSTAL_CODE_MATCHER = "postal-code-matcher"

    __str__ = str.__str__


PaymentsEnumCaptureOrStr: TypeAlias = Annotated[PaymentsEnumCapture | str, open_enum_validator(PaymentsEnumCapture)]
