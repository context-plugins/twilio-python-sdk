from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.flex_flow_enum_channel_type import FlexFlowEnumChannelTypeOrStr
from ..models.enums.flex_flow_enum_integration_type import FlexFlowEnumIntegrationTypeOrStr
from ..models.flex_v1_flex_flow import FlexV1FlexFlow
from ..models.list_flex_flow_response import ListFlexFlowResponse
from ..server.server import Server


class FlexV1FlexFlowApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1FlexFlowApiWithRawResponse(client, server, auth)

    def create_flex_flow(
        self,
        friendly_name: str,
        chat_service_sid: str,
        channel_type: FlexFlowEnumChannelTypeOrStr,
        *,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_flex_flow(
            friendly_name,
            chat_service_sid,
            channel_type,
            contact_identity=contact_identity,
            enabled=enabled,
            integration_type=integration_type,
            integration_flow_sid=integration_flow_sid,
            integration_url=integration_url,
            integration_workspace_sid=integration_workspace_sid,
            integration_workflow_sid=integration_workflow_sid,
            integration_channel=integration_channel,
            integration_timeout=integration_timeout,
            integration_priority=integration_priority,
            integration_creation_on_message=integration_creation_on_message,
            long_lived=long_lived,
            janitor_enabled=janitor_enabled,
            integration_retry_count=integration_retry_count,
            request_options=request_options,
        ).unwrap()

    def delete_flex_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_flex_flow(sid, request_options=request_options).unwrap()

    def fetch_flex_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_flex_flow(sid, request_options=request_options).unwrap()

    def list_flex_flow(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlexFlowResponse:
        """Flex Flow

        Args:
            friendly_name: The ``friendly_name`` of the Flex Flow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_flex_flow(
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_flex_flow(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        chat_service_sid: str | None = None,
        channel_type: FlexFlowEnumChannelTypeOrStr | None = None,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to update.
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_flex_flow(
            sid,
            friendly_name=friendly_name,
            chat_service_sid=chat_service_sid,
            channel_type=channel_type,
            contact_identity=contact_identity,
            enabled=enabled,
            integration_type=integration_type,
            integration_flow_sid=integration_flow_sid,
            integration_url=integration_url,
            integration_workspace_sid=integration_workspace_sid,
            integration_workflow_sid=integration_workflow_sid,
            integration_channel=integration_channel,
            integration_timeout=integration_timeout,
            integration_priority=integration_priority,
            integration_creation_on_message=integration_creation_on_message,
            long_lived=long_lived,
            janitor_enabled=janitor_enabled,
            integration_retry_count=integration_retry_count,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1FlexFlowApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1FlexFlowApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1FlexFlowApiWithRawResponse(client, server, auth)

    async def create_flex_flow(
        self,
        friendly_name: str,
        chat_service_sid: str,
        channel_type: FlexFlowEnumChannelTypeOrStr,
        *,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_flex_flow(
                friendly_name,
                chat_service_sid,
                channel_type,
                contact_identity=contact_identity,
                enabled=enabled,
                integration_type=integration_type,
                integration_flow_sid=integration_flow_sid,
                integration_url=integration_url,
                integration_workspace_sid=integration_workspace_sid,
                integration_workflow_sid=integration_workflow_sid,
                integration_channel=integration_channel,
                integration_timeout=integration_timeout,
                integration_priority=integration_priority,
                integration_creation_on_message=integration_creation_on_message,
                long_lived=long_lived,
                janitor_enabled=janitor_enabled,
                integration_retry_count=integration_retry_count,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_flex_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_flex_flow(sid, request_options=request_options)).unwrap()

    async def fetch_flex_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_flex_flow(sid, request_options=request_options)).unwrap()

    async def list_flex_flow(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlexFlowResponse:
        """Flex Flow

        Args:
            friendly_name: The ``friendly_name`` of the Flex Flow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_flex_flow(
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_flex_flow(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        chat_service_sid: str | None = None,
        channel_type: FlexFlowEnumChannelTypeOrStr | None = None,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1FlexFlow:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to update.
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_flex_flow(
                sid,
                friendly_name=friendly_name,
                chat_service_sid=chat_service_sid,
                channel_type=channel_type,
                contact_identity=contact_identity,
                enabled=enabled,
                integration_type=integration_type,
                integration_flow_sid=integration_flow_sid,
                integration_url=integration_url,
                integration_workspace_sid=integration_workspace_sid,
                integration_workflow_sid=integration_workflow_sid,
                integration_channel=integration_channel,
                integration_timeout=integration_timeout,
                integration_priority=integration_priority,
                integration_creation_on_message=integration_creation_on_message,
                long_lived=long_lived,
                janitor_enabled=janitor_enabled,
                integration_retry_count=integration_retry_count,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1FlexFlowApiWithRawResponse:
        return self._with_raw_response


class FlexV1FlexFlowApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_flex_flow(
        self,
        friendly_name: str,
        chat_service_sid: str,
        channel_type: FlexFlowEnumChannelTypeOrStr,
        *,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/FlexFlows"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("ChatServiceSid", chat_service_sid),
                    param[FlexFlowEnumChannelTypeOrStr]("ChannelType", channel_type),
                    param[str | None]("ContactIdentity", contact_identity),
                    param[bool | None]("Enabled", enabled),
                    param[FlexFlowEnumIntegrationTypeOrStr | None]("IntegrationType", integration_type),
                    param[str | None]("Integration.FlowSid", integration_flow_sid),
                    param[str | None]("Integration.Url", integration_url),
                    param[str | None]("Integration.WorkspaceSid", integration_workspace_sid),
                    param[str | None]("Integration.WorkflowSid", integration_workflow_sid),
                    param[str | None]("Integration.Channel", integration_channel),
                    param[int | None]("Integration.Timeout", integration_timeout),
                    param[int | None]("Integration.Priority", integration_priority),
                    param[bool | None]("Integration.CreationOnMessage", integration_creation_on_message),
                    param[bool | None]("LongLived", long_lived),
                    param[bool | None]("JanitorEnabled", janitor_enabled),
                    param[int | None]("Integration.RetryCount", integration_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_flex_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_flex_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_flex_flow(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlexFlowResponse, RawError]:
        """Flex Flow

        Args:
            friendly_name: The ``friendly_name`` of the Flex Flow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/FlexFlows"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlexFlowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_flex_flow(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        chat_service_sid: str | None = None,
        channel_type: FlexFlowEnumChannelTypeOrStr | None = None,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to update.
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ChatServiceSid", chat_service_sid),
                    param[FlexFlowEnumChannelTypeOrStr | None]("ChannelType", channel_type),
                    param[str | None]("ContactIdentity", contact_identity),
                    param[bool | None]("Enabled", enabled),
                    param[FlexFlowEnumIntegrationTypeOrStr | None]("IntegrationType", integration_type),
                    param[str | None]("Integration.FlowSid", integration_flow_sid),
                    param[str | None]("Integration.Url", integration_url),
                    param[str | None]("Integration.WorkspaceSid", integration_workspace_sid),
                    param[str | None]("Integration.WorkflowSid", integration_workflow_sid),
                    param[str | None]("Integration.Channel", integration_channel),
                    param[int | None]("Integration.Timeout", integration_timeout),
                    param[int | None]("Integration.Priority", integration_priority),
                    param[bool | None]("Integration.CreationOnMessage", integration_creation_on_message),
                    param[bool | None]("LongLived", long_lived),
                    param[bool | None]("JanitorEnabled", janitor_enabled),
                    param[int | None]("Integration.RetryCount", integration_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1FlexFlowApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_flex_flow(
        self,
        friendly_name: str,
        chat_service_sid: str,
        channel_type: FlexFlowEnumChannelTypeOrStr,
        *,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/FlexFlows"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("ChatServiceSid", chat_service_sid),
                    param[FlexFlowEnumChannelTypeOrStr]("ChannelType", channel_type),
                    param[str | None]("ContactIdentity", contact_identity),
                    param[bool | None]("Enabled", enabled),
                    param[FlexFlowEnumIntegrationTypeOrStr | None]("IntegrationType", integration_type),
                    param[str | None]("Integration.FlowSid", integration_flow_sid),
                    param[str | None]("Integration.Url", integration_url),
                    param[str | None]("Integration.WorkspaceSid", integration_workspace_sid),
                    param[str | None]("Integration.WorkflowSid", integration_workflow_sid),
                    param[str | None]("Integration.Channel", integration_channel),
                    param[int | None]("Integration.Timeout", integration_timeout),
                    param[int | None]("Integration.Priority", integration_priority),
                    param[bool | None]("Integration.CreationOnMessage", integration_creation_on_message),
                    param[bool | None]("LongLived", long_lived),
                    param[bool | None]("JanitorEnabled", janitor_enabled),
                    param[int | None]("Integration.RetryCount", integration_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_flex_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_flex_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_flex_flow(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlexFlowResponse, RawError]:
        """Flex Flow

        Args:
            friendly_name: The ``friendly_name`` of the Flex Flow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/FlexFlows"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlexFlowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_flex_flow(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        chat_service_sid: str | None = None,
        channel_type: FlexFlowEnumChannelTypeOrStr | None = None,
        contact_identity: str | None = None,
        enabled: bool | None = None,
        integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None,
        integration_flow_sid: str | None = None,
        integration_url: str | None = None,
        integration_workspace_sid: str | None = None,
        integration_workflow_sid: str | None = None,
        integration_channel: str | None = None,
        integration_timeout: int | None = None,
        integration_priority: int | None = None,
        integration_creation_on_message: bool | None = None,
        long_lived: bool | None = None,
        janitor_enabled: bool | None = None,
        integration_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1FlexFlow, RawError]:
        """Flex Flow

        Args:
            sid: The SID of the Flex Flow resource to update.
            friendly_name: A descriptive string that you create to describe the Flex Flow resource.
            chat_service_sid: The SID of the chat service.
            channel_type: The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``.
                By default, Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on
                this Flex Flow. The Task attributes will be used by the Flex UI to render the respective Task as
                appropriate (applying channel-specific design and length limits). If ``channelType`` is ``facebook``,
                ``whatsapp`` or ``line``, the Send to Flex widget should set the Task Channel to Programmable Chat.
            contact_identity: The channel contact's Identity.
            enabled: Whether the new Flex Flow is enabled.
            integration_type: The software that will handle inbound messages. `Integration Type
                <https://www.twilio.com/docs/flex/developer/messaging/manage-flows#integration-types>`__ can be:
                ``studio``, ``external``, or ``task``.
            integration_flow_sid: The SID of the Studio Flow. Required when ``integrationType`` is ``studio``.
            integration_url: The URL of the external webhook. Required when ``integrationType`` is ``external``.
            integration_workspace_sid: The Workspace SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_workflow_sid: The Workflow SID for a new Task. Required when ``integrationType`` is ``task``.
            integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., ``sms``) to use for the Task that
                will be created. Applicable and required when ``integrationType`` is ``task``. The default value is
                ``default``.
            integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours).
                Optional when ``integrationType`` is ``task``, not applicable otherwise.
            integration_priority: The Task priority of a new Task. The default priority is 0. Optional when
                ``integrationType`` is ``task``, not applicable otherwise.
            integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task
                immediately (and therefore reserve the conversation to current agent), or delay Task creation until the
                customer sends the first response. Set to false to create immediately, true to delay Task creation. This
                setting is only applicable for outbound messaging.
            long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent
                interactions with a contact identity. Defaults to ``false``.
            janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the
                associated Task is deleted outside of the Flex UI. Defaults to ``false``.
            integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes
                integer values from 0 to 3 with the default being 3. Optional when ``integrationType`` is ``studio`` or
                ``external``, not applicable otherwise.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/FlexFlows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ChatServiceSid", chat_service_sid),
                    param[FlexFlowEnumChannelTypeOrStr | None]("ChannelType", channel_type),
                    param[str | None]("ContactIdentity", contact_identity),
                    param[bool | None]("Enabled", enabled),
                    param[FlexFlowEnumIntegrationTypeOrStr | None]("IntegrationType", integration_type),
                    param[str | None]("Integration.FlowSid", integration_flow_sid),
                    param[str | None]("Integration.Url", integration_url),
                    param[str | None]("Integration.WorkspaceSid", integration_workspace_sid),
                    param[str | None]("Integration.WorkflowSid", integration_workflow_sid),
                    param[str | None]("Integration.Channel", integration_channel),
                    param[int | None]("Integration.Timeout", integration_timeout),
                    param[int | None]("Integration.Priority", integration_priority),
                    param[bool | None]("Integration.CreationOnMessage", integration_creation_on_message),
                    param[bool | None]("LongLived", long_lived),
                    param[bool | None]("JanitorEnabled", janitor_enabled),
                    param[int | None]("Integration.RetryCount", integration_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1FlexFlow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
