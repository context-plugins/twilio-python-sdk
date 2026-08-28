from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.interaction_channel_enum_channel_status import InteractionChannelEnumChannelStatusOrStr
from .enums.interaction_channel_enum_type import InteractionChannelEnumTypeOrStr


class FlexV1InteractionInteractionChannel(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO."""

    interaction_sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify an Interaction resource, prefixed with KD."""

    type_: Optional[InteractionChannelEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The Interaction Channel's type. Can be: ``sms``, ``email``, ``chat``, ``whatsapp``, ``web``, ``messenger``, or
    ``gbm``.
     **Note:** These can be different from the task channel type specified in the Routing attributes. Task channel type
        corresponds to channel capacity while this channel type is the actual media type"""

    status: Optional[InteractionChannelEnumChannelStatusOrStr] = UNSET
    """The status of this channel."""

    error_code: OptionalNullable[int] = UNSET
    """The Twilio error code for a failed channel."""

    error_message: OptionalNullable[str] = UNSET
    """The error message for a failed channel."""

    url: OptionalNullable[AnyUrl] = UNSET
    links: OptionalNullable[Any] = UNSET


class FlexV1InteractionInteractionChannelDict(TypedDict):
    sid: NotRequired[str | None]
    interaction_sid: NotRequired[str | None]
    type_: NotRequired[InteractionChannelEnumTypeOrStr]
    status: NotRequired[InteractionChannelEnumChannelStatusOrStr]
    error_code: NotRequired[int | None]
    error_message: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
