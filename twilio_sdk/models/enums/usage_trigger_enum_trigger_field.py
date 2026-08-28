from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UsageTriggerEnumTriggerField(str, Enum):
    """The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource that fires the
    trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords documentation
    <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__."""

    COUNT = "count"
    USAGE = "usage"
    PRICE = "price"

    __str__ = str.__str__


UsageTriggerEnumTriggerFieldOrStr: TypeAlias = Annotated[
    UsageTriggerEnumTriggerField | str, open_enum_validator(UsageTriggerEnumTriggerField)
]
