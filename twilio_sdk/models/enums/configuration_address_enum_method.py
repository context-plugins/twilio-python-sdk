from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConfigurationAddressEnumMethod(str, Enum):
    GET = "get"
    POST = "post"

    __str__ = str.__str__


ConfigurationAddressEnumMethodOrStr: TypeAlias = Annotated[
    ConfigurationAddressEnumMethod | str, open_enum_validator(ConfigurationAddressEnumMethod)
]
