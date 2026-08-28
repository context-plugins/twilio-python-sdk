from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceConversationScopedWebhookEnumMethod(str, Enum):
    GET = "get"
    POST = "post"

    __str__ = str.__str__


ServiceConversationScopedWebhookEnumMethodOrStr: TypeAlias = Annotated[
    ServiceConversationScopedWebhookEnumMethod | str, open_enum_validator(ServiceConversationScopedWebhookEnumMethod)
]
