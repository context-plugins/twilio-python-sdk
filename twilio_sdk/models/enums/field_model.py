from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FieldModel(str, Enum):
    CALLER_NAME = "caller_name"
    SIM_SWAP = "sim_swap"
    CALL_FORWARDING = "call_forwarding"
    LINE_TYPE_INTELLIGENCE = "line_type_intelligence"
    LINE_STATUS = "line_status"
    IDENTITY_MATCH = "identity_match"
    REASSIGNED_NUMBER = "reassigned_number"
    SMS_PUMPING_RISK = "sms_pumping_risk"

    __str__ = str.__str__


FieldModelOrStr: TypeAlias = Annotated[FieldModel | str, open_enum_validator(FieldModel)]
