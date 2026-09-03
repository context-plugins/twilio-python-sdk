from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_plugin_configuration_configured_plugin import FlexV1PluginConfigurationConfiguredPlugin
from ..models.list_configured_plugin_response import ListConfiguredPluginResponse
from ..server.server import Server


class FlexV1ConfiguredPlugin:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1ConfiguredPluginWithRawResponse(client, server, auth)

    def fetch_configured_plugin(
        self,
        configuration_sid: str,
        plugin_sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginConfigurationConfiguredPlugin:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            plugin_sid: The unique string that we created to identify the Flex Plugin resource.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_configured_plugin(
            configuration_sid, plugin_sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def list_configured_plugin(
        self,
        configuration_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConfiguredPluginResponse:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_configured_plugin(
            configuration_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            flex_metadata=flex_metadata,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1ConfiguredPluginWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1ConfiguredPlugin:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1ConfiguredPluginWithRawResponse(client, server, auth)

    async def fetch_configured_plugin(
        self,
        configuration_sid: str,
        plugin_sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginConfigurationConfiguredPlugin:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            plugin_sid: The unique string that we created to identify the Flex Plugin resource.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_configured_plugin(
                configuration_sid, plugin_sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def list_configured_plugin(
        self,
        configuration_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConfiguredPluginResponse:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
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
            await self._with_raw_response.list_configured_plugin(
                configuration_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                flex_metadata=flex_metadata,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1ConfiguredPluginWithRawResponse:
        return self._with_raw_response


class FlexV1ConfiguredPluginWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_configured_plugin(
        self,
        configuration_sid: str,
        plugin_sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginConfigurationConfiguredPlugin, RawError]:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            plugin_sid: The unique string that we created to identify the Flex Plugin resource.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/v1/PluginService/Configurations/{ConfigurationSid}/Plugins/{PluginSid}"
            ),
            path_params=[param[str]("ConfigurationSid", configuration_sid), param[str]("PluginSid", plugin_sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfigurationConfiguredPlugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_configured_plugin(
        self,
        configuration_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConfiguredPluginResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations/{ConfigurationSid}/Plugins"),
            path_params=[param[str]("ConfigurationSid", configuration_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConfiguredPluginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1ConfiguredPluginWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_configured_plugin(
        self,
        configuration_sid: str,
        plugin_sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginConfigurationConfiguredPlugin, RawError]:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            plugin_sid: The unique string that we created to identify the Flex Plugin resource.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/v1/PluginService/Configurations/{ConfigurationSid}/Plugins/{PluginSid}"
            ),
            path_params=[param[str]("ConfigurationSid", configuration_sid), param[str]("PluginSid", plugin_sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfigurationConfiguredPlugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_configured_plugin(
        self,
        configuration_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConfiguredPluginResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            configuration_sid: The SID of the Flex Plugin Configuration the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Configurations/{ConfigurationSid}/Plugins"),
            path_params=[param[str]("ConfigurationSid", configuration_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConfiguredPluginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
