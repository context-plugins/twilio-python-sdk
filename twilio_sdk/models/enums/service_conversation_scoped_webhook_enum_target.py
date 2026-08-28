from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceConversationScopedWebhookEnumTarget(str, Enum):
    """The target of this webhook: ``webhook``, ``studio``, ``trigger``"""

    WEBHOOK = "webhook"
    TRIGGER = "trigger"
    STUDIO = "studio"

    __str__ = str.__str__


ServiceConversationScopedWebhookEnumTargetOrStr: TypeAlias = Annotated[
    ServiceConversationScopedWebhookEnumTarget | str, open_enum_validator(ServiceConversationScopedWebhookEnumTarget)
]
