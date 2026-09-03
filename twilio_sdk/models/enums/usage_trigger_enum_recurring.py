from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UsageTriggerEnumRecurring(str, Enum):
    """The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for recurring triggers
    or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in
    GMT."""

    DAILY = "daily"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    ALLTIME = "alltime"

    __str__ = str.__str__


UsageTriggerEnumRecurringOrStr: TypeAlias = Annotated[
    UsageTriggerEnumRecurring | str, open_enum_validator(UsageTriggerEnumRecurring)
]
