from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.flex_flow_enum_channel_type import FlexFlowEnumChannelTypeOrStr
from .enums.flex_flow_enum_integration_type import FlexFlowEnumIntegrationTypeOrStr


class FlexV1FlexFlow(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Flow resource and
    owns this Workflow."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Flex Flow resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the chat service."""

    channel_type: Optional[FlexFlowEnumChannelTypeOrStr] = UNSET
    """The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``. By default,
    Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on this Flex Flow. The Task
    attributes will be used by the Flex UI to render the respective Task as appropriate (applying channel-specific
    design and length limits). If ``channelType`` is ``facebook``, ``whatsapp`` or ``line``, the Send to Flex widget
    should set the Task Channel to Programmable Chat."""

    contact_identity: OptionalNullable[str] = UNSET
    """The channel contact's Identity."""

    enabled: OptionalNullable[bool] = UNSET
    """Whether the Flex Flow is enabled."""

    integration_type: Optional[FlexFlowEnumIntegrationTypeOrStr] = UNSET
    """The software that will handle inbound messages. `Integration Type
    <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be: ``studio``,
    ``external``, or ``task``."""

    integration: OptionalNullable[Any] = UNSET
    """An object that contains specific parameters for the integration."""

    long_lived: OptionalNullable[bool] = UNSET
    """When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a
    contact identity. Defaults to ``false``."""

    janitor_enabled: OptionalNullable[bool] = UNSET
    """When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted
    outside of the Flex UI. Defaults to ``false``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Flex Flow resource."""


class FlexV1FlexFlowDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    channel_type: NotRequired[FlexFlowEnumChannelTypeOrStr]
    contact_identity: NotRequired[str | None]
    enabled: NotRequired[bool | None]
    integration_type: NotRequired[FlexFlowEnumIntegrationTypeOrStr]
    integration: NotRequired[Any | None]
    long_lived: NotRequired[bool | None]
    janitor_enabled: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
