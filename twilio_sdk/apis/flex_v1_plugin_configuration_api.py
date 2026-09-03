from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_plugin_configuration import FlexV1PluginConfiguration
from ..models.list_plugin_configuration_response import ListPluginConfigurationResponse
from ..server.server import Server


class FlexV1PluginConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginConfigurationApiWithRawResponse(client, server, auth)

    def create_plugin_configuration(
        self,
        name: str,
        *,
        flex_metadata: str | None = None,
        plugins: list[Any] | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginConfiguration:
        """Send a ``POST`` request.

        Args:
            name: The Flex Plugin Configuration's name.
            flex_metadata: The Flex-Metadata HTTP request header
            plugins: A list of objects that describe the plugin versions included in the configuration. Each object
                contains the sid of the plugin version.
            description: The Flex Plugin Configuration's description.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_plugin_configuration(
            name, flex_metadata=flex_metadata, plugins=plugins, description=description, request_options=request_options
        ).unwrap()

    def fetch_plugin_configuration(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginConfiguration:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_plugin_configuration(
            sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def list_plugin_configuration(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginConfigurationResponse:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_plugin_configuration(
            page_size=page_size,
            page=page,
            page_token=page_token,
            flex_metadata=flex_metadata,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginConfigurationApiWithRawResponse(client, server, auth)

    async def create_plugin_configuration(
        self,
        name: str,
        *,
        flex_metadata: str | None = None,
        plugins: list[Any] | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginConfiguration:
        """Send a ``POST`` request.

        Args:
            name: The Flex Plugin Configuration's name.
            flex_metadata: The Flex-Metadata HTTP request header
            plugins: A list of objects that describe the plugin versions included in the configuration. Each object
                contains the sid of the plugin version.
            description: The Flex Plugin Configuration's description.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_plugin_configuration(
                name,
                flex_metadata=flex_metadata,
                plugins=plugins,
                description=description,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_plugin_configuration(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginConfiguration:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_plugin_configuration(
                sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def list_plugin_configuration(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginConfigurationResponse:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_plugin_configuration(
                page_size=page_size,
                page=page,
                page_token=page_token,
                flex_metadata=flex_metadata,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginConfigurationApiWithRawResponse:
        return self._with_raw_response


class FlexV1PluginConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_plugin_configuration(
        self,
        name: str,
        *,
        flex_metadata: str | None = None,
        plugins: list[Any] | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginConfiguration, RawError]:
        """Send a ``POST`` request.

        Args:
            name: The Flex Plugin Configuration's name.
            flex_metadata: The Flex-Metadata HTTP request header
            plugins: A list of objects that describe the plugin versions included in the configuration. Each object
                contains the sid of the plugin version.
            description: The Flex Plugin Configuration's description.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Configurations"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Name", name),
                    param[list[Any] | None]("Plugins", plugins),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_plugin_configuration(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginConfiguration, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_plugin_configuration(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginConfigurationResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginConfigurationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_plugin_configuration(
        self,
        name: str,
        *,
        flex_metadata: str | None = None,
        plugins: list[Any] | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginConfiguration, RawError]:
        """Send a ``POST`` request.

        Args:
            name: The Flex Plugin Configuration's name.
            flex_metadata: The Flex-Metadata HTTP request header
            plugins: A list of objects that describe the plugin versions included in the configuration. Each object
                contains the sid of the plugin version.
            description: The Flex Plugin Configuration's description.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Configurations"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Name", name),
                    param[list[Any] | None]("Plugins", plugins),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_plugin_configuration(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginConfiguration, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_plugin_configuration(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginConfigurationResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
