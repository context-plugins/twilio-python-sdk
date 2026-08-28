from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .configuration_event import ConfigurationEvent, ConfigurationEventDict


class ConfigurationsRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    configurations: ConfigurationEvent


class ConfigurationsRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    configurations: ConfigurationEvent | ConfigurationEventDict
