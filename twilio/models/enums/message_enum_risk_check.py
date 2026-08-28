from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumRiskCheck(str, Enum):
    """Include this parameter with a value of ``disable`` to skip any kind of risk check on the respective message
    request., Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per verification
    attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass active protections if
    disabled. Can be: ``enable``(default) or ``disable``. For SMS channel only."""

    ENABLE = "enable"
    DISABLE = "disable"

    __str__ = str.__str__


MessageEnumRiskCheckOrStr: TypeAlias = Annotated[MessageEnumRiskCheck | str, open_enum_validator(MessageEnumRiskCheck)]
