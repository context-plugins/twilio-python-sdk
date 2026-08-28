from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookEnumStatus(str, Enum):
    """The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``"""

    ENABLED = "enabled"
    DISABLED = "disabled"

    __str__ = str.__str__


WebhookEnumStatusOrStr: TypeAlias = Annotated[WebhookEnumStatus | str, open_enum_validator(WebhookEnumStatus)]
