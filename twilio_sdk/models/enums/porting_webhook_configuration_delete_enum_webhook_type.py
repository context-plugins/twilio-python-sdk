from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PortingWebhookConfigurationDeleteEnumWebhookType(str, Enum):
    """The of the webhook type of the configuration to be deleted"""

    PORT_IN = "PORT_IN"
    PORT_OUT = "PORT_OUT"

    __str__ = str.__str__


PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr: TypeAlias = Annotated[
    PortingWebhookConfigurationDeleteEnumWebhookType | str,
    open_enum_validator(PortingWebhookConfigurationDeleteEnumWebhookType),
]
