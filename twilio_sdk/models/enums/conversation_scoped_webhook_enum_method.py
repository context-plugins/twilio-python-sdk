from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationScopedWebhookEnumMethod(str, Enum):
    GET = "get"
    POST = "post"

    __str__ = str.__str__


ConversationScopedWebhookEnumMethodOrStr: TypeAlias = Annotated[
    ConversationScopedWebhookEnumMethod | str, open_enum_validator(ConversationScopedWebhookEnumMethod)
]
