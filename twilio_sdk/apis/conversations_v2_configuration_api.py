from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_configuration_error import CreateConfigurationErrorBody, create_configuration_error_mapper
from ..errors.delete_configuration_error import DeleteConfigurationErrorBody, delete_configuration_error_mapper
from ..errors.fetch_configuration2_error import FetchConfiguration2ErrorBody, fetch_configuration2_error_mapper
from ..errors.list_configuration_error import ListConfigurationErrorBody, list_configuration_error_mapper
from ..errors.update_configuration2_error import UpdateConfiguration2ErrorBody, update_configuration2_error_mapper
from ..models.conversations_v2_configuration import ConversationsV2Configuration
from ..models.conversations_v2_operation_accepted import ConversationsV2OperationAccepted
from ..models.v2_control_plane_configurations_request import (
    V2ControlPlaneConfigurationsRequest,
    V2ControlPlaneConfigurationsRequestDict,
)
from ..models.v2_control_plane_configurations_request1 import (
    V2ControlPlaneConfigurationsRequest1,
    V2ControlPlaneConfigurationsRequest1Dict,
)
from ..models.v2_control_plane_configurations_response import V2ControlPlaneConfigurationsResponse
from ..server.server import Server


class ConversationsV2ConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2ConfigurationApiWithRawResponse(client, server, auth)

    def create_configuration(
        self,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2OperationAccepted:
        """Create a new Configuration

        Args:
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Bad Request Conflict Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_configuration(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def delete_configuration(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationAccepted:
        """Delete a Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Not Found Conflict Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.delete_configuration(
            sid, idempotency_key=idempotency_key, request_options=request_options
        ).unwrap()

    def fetch_configuration2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Configuration:
        """Retrieve a Configuration.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_configuration2(sid, request_options=request_options).unwrap()

    def list_configuration(
        self,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        memory_store_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ControlPlaneConfigurationsResponse:
        """Retrieve a list of Configurations.

        Args:
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            memory_store_id: Filter configurations by Memory Store ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.list_configuration(
            page_size=page_size, page_token=page_token, memory_store_id=memory_store_id, request_options=request_options
        ).unwrap()

    def update_configuration2(
        self,
        sid: str,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2OperationAccepted:
        """Update an existing Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.update_configuration2(
            sid, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2ConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2ConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2ConfigurationApiWithRawResponse(client, server, auth)

    async def create_configuration(
        self,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2OperationAccepted:
        """Create a new Configuration

        Args:
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Bad Request Conflict Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_configuration(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete_configuration(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationAccepted:
        """Delete a Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Not Found Conflict Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.delete_configuration(
                sid, idempotency_key=idempotency_key, request_options=request_options
            )
        ).unwrap()

    async def fetch_configuration2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Configuration:
        """Retrieve a Configuration.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (await self._with_raw_response.fetch_configuration2(sid, request_options=request_options)).unwrap()

    async def list_configuration(
        self,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        memory_store_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ControlPlaneConfigurationsResponse:
        """Retrieve a list of Configurations.

        Args:
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            memory_store_id: Filter configurations by Memory Store ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.list_configuration(
                page_size=page_size,
                page_token=page_token,
                memory_store_id=memory_store_id,
                request_options=request_options,
            )
        ).unwrap()

    async def update_configuration2(
        self,
        sid: str,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2OperationAccepted:
        """Update an existing Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted - Operation created for asynchronous processing

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.update_configuration2(
                sid, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2ConfigurationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV2ConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_configuration(
        self,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2OperationAccepted, CreateConfigurationErrorBody]:
        """Create a new Configuration

        Args:
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/ControlPlane/Configurations"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=create_configuration_error_mapper,
            request_options=request_options,
        )

    def delete_configuration(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationAccepted, DeleteConfigurationErrorBody]:
        """Delete a Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=delete_configuration_error_mapper,
            request_options=request_options,
        )

    def fetch_configuration2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Configuration, FetchConfiguration2ErrorBody]:
        """Retrieve a Configuration.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Configuration],
            error_mapper=fetch_configuration2_error_mapper,
            request_options=request_options,
        )

    def list_configuration(
        self,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        memory_store_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ControlPlaneConfigurationsResponse, ListConfigurationErrorBody]:
        """Retrieve a list of Configurations.

        Args:
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            memory_store_id: Filter configurations by Memory Store ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Configurations"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
                param[str | None]("memoryStoreId", memory_store_id),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ControlPlaneConfigurationsResponse],
            error_mapper=list_configuration_error_mapper,
            request_options=request_options,
        )

    def update_configuration2(
        self,
        sid: str,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2OperationAccepted, UpdateConfiguration2ErrorBody]:
        """Update an existing Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=update_configuration2_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2ConfigurationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_configuration(
        self,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2OperationAccepted, CreateConfigurationErrorBody]:
        """Create a new Configuration

        Args:
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/ControlPlane/Configurations"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=create_configuration_error_mapper,
            request_options=request_options,
        )

    async def delete_configuration(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationAccepted, DeleteConfigurationErrorBody]:
        """Delete a Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=delete_configuration_error_mapper,
            request_options=request_options,
        )

    async def fetch_configuration2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Configuration, FetchConfiguration2ErrorBody]:
        """Retrieve a Configuration.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Configuration],
            error_mapper=fetch_configuration2_error_mapper,
            request_options=request_options,
        )

    async def list_configuration(
        self,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        memory_store_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ControlPlaneConfigurationsResponse, ListConfigurationErrorBody]:
        """Retrieve a list of Configurations.

        Args:
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            memory_store_id: Filter configurations by Memory Store ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Configurations"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
                param[str | None]("memoryStoreId", memory_store_id),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ControlPlaneConfigurationsResponse],
            error_mapper=list_configuration_error_mapper,
            request_options=request_options,
        )

    async def update_configuration2(
        self,
        sid: str,
        *,
        idempotency_key: str | None = None,
        body: V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2OperationAccepted, UpdateConfiguration2ErrorBody]:
        """Update an existing Configuration

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            body: The configuration to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/ControlPlane/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=update_configuration2_error_mapper,
            request_options=request_options,
        )
