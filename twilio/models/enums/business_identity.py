from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessIdentity(str, Enum):
    """Business customer type"""

    DIRECT = "DIRECT"
    ISV = "ISV"

    __str__ = str.__str__


BusinessIdentityOrStr: TypeAlias = Annotated[BusinessIdentity | str, open_enum_validator(BusinessIdentity)]
