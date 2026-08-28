from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConfigurationWebhookEnumTarget(str, Enum):
    """The routing target of the webhook. Can be ordinary or route internally to Flex"""

    WEBHOOK = "webhook"
    FLEX = "flex"

    __str__ = str.__str__


ConfigurationWebhookEnumTargetOrStr: TypeAlias = Annotated[
    ConfigurationWebhookEnumTarget | str, open_enum_validator(ConfigurationWebhookEnumTarget)
]
