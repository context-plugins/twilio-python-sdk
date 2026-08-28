from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlexFlowEnumIntegrationType(str, Enum):
    """The software that will handle inbound messages. `Integration Type
    <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be: ``studio``,
    ``external``, or ``task``."""

    STUDIO = "studio"
    EXTERNAL = "external"
    TASK = "task"

    __str__ = str.__str__


FlexFlowEnumIntegrationTypeOrStr: TypeAlias = Annotated[
    FlexFlowEnumIntegrationType | str, open_enum_validator(FlexFlowEnumIntegrationType)
]
