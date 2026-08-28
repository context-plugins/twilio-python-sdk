from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConfigurationAddressEnumAutoCreationType(str, Enum):
    WEBHOOK = "webhook"
    STUDIO = "studio"
    DEFAULT = "default"

    __str__ = str.__str__


ConfigurationAddressEnumAutoCreationTypeOrStr: TypeAlias = Annotated[
    ConfigurationAddressEnumAutoCreationType | str, open_enum_validator(ConfigurationAddressEnumAutoCreationType)
]
