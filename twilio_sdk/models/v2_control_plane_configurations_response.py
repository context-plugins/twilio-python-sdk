from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .conversations_v2_configuration import ConversationsV2Configuration, ConversationsV2ConfigurationDict
from .meta1 import Meta1, Meta1Dict


class V2ControlPlaneConfigurationsResponse(SdkBaseModel):
    configurations: list[ConversationsV2Configuration]
    meta: Meta1


class V2ControlPlaneConfigurationsResponseDict(TypedDict):
    configurations: list[ConversationsV2Configuration | ConversationsV2ConfigurationDict]
    meta: Meta1 | Meta1Dict
