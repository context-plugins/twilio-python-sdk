from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerCareChannel(str, Enum):
    TOLL_FREE_NUMBER = "TOLL_FREE_NUMBER"
    EMAIL = "EMAIL"

    __str__ = str.__str__


CustomerCareChannelOrStr: TypeAlias = Annotated[CustomerCareChannel | str, open_enum_validator(CustomerCareChannel)]
