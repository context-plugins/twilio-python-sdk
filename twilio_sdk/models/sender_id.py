from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class SenderId(SdkBaseModel):
    account_sid: str
    """Account that owns the Sender ID."""

    date_created: RFC3339DateTime
    """The date and time when the Sender ID was created."""

    date_updated: RFC3339DateTime
    """The date and time when the Sender ID was last updated."""

    sender_id: str
    """The alphanumeric sender ID."""

    sid: str
    """The unique identifier of the Sender ID."""

    mps: int
    """Messages per second (throughput) for the Sender ID."""


class SenderIdDict(TypedDict):
    account_sid: str
    date_created: RFC3339DateTime
    date_updated: RFC3339DateTime
    sender_id: str
    sid: str
    mps: int
