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
from ..models.conversations_v1_configuration_address import ConversationsV1ConfigurationAddress
from ..models.enums.configuration_address_enum_auto_creation_type import ConfigurationAddressEnumAutoCreationTypeOrStr
from ..models.enums.configuration_address_enum_method import ConfigurationAddressEnumMethodOrStr
from ..models.enums.configuration_address_enum_type import ConfigurationAddressEnumTypeOrStr
from ..models.list_configuration_address_response import ListConfigurationAddressResponse
from ..server.server import Server


class ConversationsV1AddressConfiguration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1AddressConfigurationWithRawResponse(client, server, auth)

    def create_configuration_address(
        self,
        type_: ConfigurationAddressEnumTypeOrStr,
        address: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        address_country: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationAddress:
        """Create a new address configuration

        Args:
            type_: Type of Address, value can be ``whatsapp`` or ``sms``.
            address: The unique address to be configured. The address can be a whatsapp address or phone number
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            address_country: An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only
                applicable to short code addresses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_configuration_address(
            type_,
            address,
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
            address_country=address_country,
            request_options=request_options,
        ).unwrap()

    def delete_configuration_address(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_configuration_address(sid, request_options=request_options).unwrap()

    def fetch_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConfigurationAddress:
        """Fetch an address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_configuration_address(sid, request_options=request_options).unwrap()

    def list_configuration_address(
        self,
        *,
        type_: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConfigurationAddressResponse:
        """Retrieve a list of address configurations for an account

        Args:
            type_: Filter the address configurations by its type. This value can be one of: ``whatsapp``, ``sms``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_configuration_address(
            type_=type_, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_configuration_address(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationAddress:
        """Update an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_configuration_address(
            sid,
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1AddressConfigurationWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1AddressConfiguration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1AddressConfigurationWithRawResponse(client, server, auth)

    async def create_configuration_address(
        self,
        type_: ConfigurationAddressEnumTypeOrStr,
        address: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        address_country: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationAddress:
        """Create a new address configuration

        Args:
            type_: Type of Address, value can be ``whatsapp`` or ``sms``.
            address: The unique address to be configured. The address can be a whatsapp address or phone number
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            address_country: An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only
                applicable to short code addresses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_configuration_address(
                type_,
                address,
                friendly_name=friendly_name,
                auto_creation_enabled=auto_creation_enabled,
                auto_creation_type=auto_creation_type,
                auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
                auto_creation_webhook_url=auto_creation_webhook_url,
                auto_creation_webhook_method=auto_creation_webhook_method,
                auto_creation_webhook_filters=auto_creation_webhook_filters,
                auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
                auto_creation_studio_retry_count=auto_creation_studio_retry_count,
                address_country=address_country,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_configuration_address(sid, request_options=request_options)
        ).unwrap()

    async def fetch_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConfigurationAddress:
        """Fetch an address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_configuration_address(sid, request_options=request_options)
        ).unwrap()

    async def list_configuration_address(
        self,
        *,
        type_: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConfigurationAddressResponse:
        """Retrieve a list of address configurations for an account

        Args:
            type_: Filter the address configurations by its type. This value can be one of: ``whatsapp``, ``sms``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_configuration_address(
                type_=type_, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_configuration_address(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationAddress:
        """Update an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_configuration_address(
                sid,
                friendly_name=friendly_name,
                auto_creation_enabled=auto_creation_enabled,
                auto_creation_type=auto_creation_type,
                auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
                auto_creation_webhook_url=auto_creation_webhook_url,
                auto_creation_webhook_method=auto_creation_webhook_method,
                auto_creation_webhook_filters=auto_creation_webhook_filters,
                auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
                auto_creation_studio_retry_count=auto_creation_studio_retry_count,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1AddressConfigurationWithRawResponse:
        return self._with_raw_response


class ConversationsV1AddressConfigurationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_configuration_address(
        self,
        type_: ConfigurationAddressEnumTypeOrStr,
        address: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        address_country: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Create a new address configuration

        Args:
            type_: Type of Address, value can be ``whatsapp`` or ``sms``.
            address: The unique address to be configured. The address can be a whatsapp address or phone number
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            address_country: An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only
                applicable to short code addresses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Addresses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[ConfigurationAddressEnumTypeOrStr]("Type", type_),
                    param[str]("Address", address),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("AutoCreation.Enabled", auto_creation_enabled),
                    param[ConfigurationAddressEnumAutoCreationTypeOrStr | None](
                        "AutoCreation.Type", auto_creation_type
                    ),
                    param[str | None]("AutoCreation.ConversationServiceSid", auto_creation_conversation_service_sid),
                    param[str | None]("AutoCreation.WebhookUrl", auto_creation_webhook_url),
                    param[ConfigurationAddressEnumMethodOrStr | None](
                        "AutoCreation.WebhookMethod", auto_creation_webhook_method
                    ),
                    param[list[str] | None]("AutoCreation.WebhookFilters", auto_creation_webhook_filters),
                    param[str | None]("AutoCreation.StudioFlowSid", auto_creation_studio_flow_sid),
                    param[int | None]("AutoCreation.StudioRetryCount", auto_creation_studio_retry_count),
                    param[str | None]("AddressCountry", address_country),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Fetch an address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_configuration_address(
        self,
        *,
        type_: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConfigurationAddressResponse, RawError]:
        """Retrieve a list of address configurations for an account

        Args:
            type_: Filter the address configurations by its type. This value can be one of: ``whatsapp``, ``sms``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Addresses"),
            query_params=[
                param[str | None]("Type", type_),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConfigurationAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_configuration_address(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Update an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("AutoCreation.Enabled", auto_creation_enabled),
                    param[ConfigurationAddressEnumAutoCreationTypeOrStr | None](
                        "AutoCreation.Type", auto_creation_type
                    ),
                    param[str | None]("AutoCreation.ConversationServiceSid", auto_creation_conversation_service_sid),
                    param[str | None]("AutoCreation.WebhookUrl", auto_creation_webhook_url),
                    param[ConfigurationAddressEnumMethodOrStr | None](
                        "AutoCreation.WebhookMethod", auto_creation_webhook_method
                    ),
                    param[list[str] | None]("AutoCreation.WebhookFilters", auto_creation_webhook_filters),
                    param[str | None]("AutoCreation.StudioFlowSid", auto_creation_studio_flow_sid),
                    param[int | None]("AutoCreation.StudioRetryCount", auto_creation_studio_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1AddressConfigurationWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_configuration_address(
        self,
        type_: ConfigurationAddressEnumTypeOrStr,
        address: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        address_country: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Create a new address configuration

        Args:
            type_: Type of Address, value can be ``whatsapp`` or ``sms``.
            address: The unique address to be configured. The address can be a whatsapp address or phone number
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            address_country: An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only
                applicable to short code addresses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Addresses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[ConfigurationAddressEnumTypeOrStr]("Type", type_),
                    param[str]("Address", address),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("AutoCreation.Enabled", auto_creation_enabled),
                    param[ConfigurationAddressEnumAutoCreationTypeOrStr | None](
                        "AutoCreation.Type", auto_creation_type
                    ),
                    param[str | None]("AutoCreation.ConversationServiceSid", auto_creation_conversation_service_sid),
                    param[str | None]("AutoCreation.WebhookUrl", auto_creation_webhook_url),
                    param[ConfigurationAddressEnumMethodOrStr | None](
                        "AutoCreation.WebhookMethod", auto_creation_webhook_method
                    ),
                    param[list[str] | None]("AutoCreation.WebhookFilters", auto_creation_webhook_filters),
                    param[str | None]("AutoCreation.StudioFlowSid", auto_creation_studio_flow_sid),
                    param[int | None]("AutoCreation.StudioRetryCount", auto_creation_studio_retry_count),
                    param[str | None]("AddressCountry", address_country),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_configuration_address(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Fetch an address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_configuration_address(
        self,
        *,
        type_: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConfigurationAddressResponse, RawError]:
        """Retrieve a list of address configurations for an account

        Args:
            type_: Filter the address configurations by its type. This value can be one of: ``whatsapp``, ``sms``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Addresses"),
            query_params=[
                param[str | None]("Type", type_),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConfigurationAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_configuration_address(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        auto_creation_enabled: bool | None = None,
        auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None,
        auto_creation_conversation_service_sid: str | None = None,
        auto_creation_webhook_url: str | None = None,
        auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None,
        auto_creation_webhook_filters: list[str] | None = None,
        auto_creation_studio_flow_sid: str | None = None,
        auto_creation_studio_retry_count: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationAddress, RawError]:
        """Update an existing address configuration

        Args:
            sid: The SID of the Address Configuration resource. This value can be either the ``sid`` or the ``address``
                of the configuration
            friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
            auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
            auto_creation_type: Value sent with the request.
            auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set,
                the conversation is created in the default service.
            auto_creation_webhook_url: For type ``webhook``, the url for the webhook request.
            auto_creation_webhook_method: Value sent with the request.
            auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be
                any of the following: ``onMessageAdded``, ``onMessageUpdated``, ``onMessageRemoved``,
                ``onConversationUpdated``, ``onConversationStateUpdated``, ``onConversationRemoved``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onDeliveryUpdated``
            auto_creation_studio_flow_sid: For type ``studio``, the studio flow SID where the webhook should be sent to.
            auto_creation_studio_retry_count: For type ``studio``, number of times to retry the webhook request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Addresses/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("AutoCreation.Enabled", auto_creation_enabled),
                    param[ConfigurationAddressEnumAutoCreationTypeOrStr | None](
                        "AutoCreation.Type", auto_creation_type
                    ),
                    param[str | None]("AutoCreation.ConversationServiceSid", auto_creation_conversation_service_sid),
                    param[str | None]("AutoCreation.WebhookUrl", auto_creation_webhook_url),
                    param[ConfigurationAddressEnumMethodOrStr | None](
                        "AutoCreation.WebhookMethod", auto_creation_webhook_method
                    ),
                    param[list[str] | None]("AutoCreation.WebhookFilters", auto_creation_webhook_filters),
                    param[str | None]("AutoCreation.StudioFlowSid", auto_creation_studio_flow_sid),
                    param[int | None]("AutoCreation.StudioRetryCount", auto_creation_studio_retry_count),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
