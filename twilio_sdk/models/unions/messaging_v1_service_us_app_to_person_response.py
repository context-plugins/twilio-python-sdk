from __future__ import annotations

from typing import TypeAlias

from ..messaging_v1_service_us_app_to_person import MessagingV1ServiceUsAppToPerson, MessagingV1ServiceUsAppToPersonDict
from ..messaging_v1_service_us_app_to_person_v2 import (
    MessagingV1ServiceUsAppToPersonV2,
    MessagingV1ServiceUsAppToPersonV2Dict,
)

MessagingV1ServiceUsAppToPersonResponse: TypeAlias = MessagingV1ServiceUsAppToPerson | MessagingV1ServiceUsAppToPersonV2

MessagingV1ServiceUsAppToPersonResponseDict: TypeAlias = (
    MessagingV1ServiceUsAppToPersonDict | MessagingV1ServiceUsAppToPersonV2Dict
)
