from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Transport(str, Enum):
    USB = "usb"
    NFC = "nfc"
    BLE = "ble"
    SMART_CARD = "smart-card"
    INTERNAL = "internal"
    HYBRID = "hybrid"

    __str__ = str.__str__


TransportOrStr: TypeAlias = Annotated[Transport | str, open_enum_validator(Transport)]
