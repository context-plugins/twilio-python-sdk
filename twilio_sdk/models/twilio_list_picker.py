from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_item import ListItem, ListItemDict


class TwilioListPicker(SdkBaseModel):
    """twilio/list-picker includes a menu of up to 10 options, which offers a simple way for users to make a
    selection."""

    body: str
    button: str
    items: list[ListItem]


class TwilioListPickerDict(TypedDict):
    body: str
    button: str
    items: list[ListItem | ListItemDict]
