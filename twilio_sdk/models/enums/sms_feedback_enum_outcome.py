from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsFeedbackEnumOutcome(str, Enum):
    CONFIRMED = "confirmed"
    UNCONFIRMED = "unconfirmed"
    RECEIVED = "received"
    NOT_RECEIVED = "not-received"
    DELAYED = "delayed"

    __str__ = str.__str__


SmsFeedbackEnumOutcomeOrStr: TypeAlias = Annotated[
    SmsFeedbackEnumOutcome | str, open_enum_validator(SmsFeedbackEnumOutcome)
]
