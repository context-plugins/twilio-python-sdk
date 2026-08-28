from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EvaluationEnumStatus(str, Enum):
    """The compliance status of the Evaluation resource."""

    COMPLIANT = "compliant"
    NONCOMPLIANT = "noncompliant"

    __str__ = str.__str__


EvaluationEnumStatusOrStr: TypeAlias = Annotated[EvaluationEnumStatus | str, open_enum_validator(EvaluationEnumStatus)]
