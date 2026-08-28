from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentFrequency(str, Enum):
    QUARTERLY = "QUARTERLY"
    YEARLY = "YEARLY"

    __str__ = str.__str__


PaymentFrequencyOrStr: TypeAlias = Annotated[PaymentFrequency | str, open_enum_validator(PaymentFrequency)]
