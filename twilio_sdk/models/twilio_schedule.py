from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TwilioSchedule(SdkBaseModel):
    """twilio/schedule templates allow us to send a message with a schedule with different time slots"""

    id: str
    title: str
    time_slots: str = Field(alias="timeSlots")


class TwilioScheduleDict(TypedDict):
    id: str
    title: str
    time_slots: str
