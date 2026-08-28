from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Confirmation(str, Enum):
    """Whether to prompt the caller to confirm their payment information before submitting to the payment gateway. If
    ``true``, the caller will hear the last 4 digits of their card or account number and must press 1 to confirm or 2 to
    cancel. Default is ``false``."""

    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


ConfirmationOrStr: TypeAlias = Annotated[Confirmation | str, open_enum_validator(Confirmation)]
