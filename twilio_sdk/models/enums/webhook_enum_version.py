from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookEnumVersion(str, Enum):
    """The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1`` is legacy and
    may be removed in the future."""

    V1 = "v1"
    V2 = "v2"

    __str__ = str.__str__


WebhookEnumVersionOrStr: TypeAlias = Annotated[WebhookEnumVersion | str, open_enum_validator(WebhookEnumVersion)]
