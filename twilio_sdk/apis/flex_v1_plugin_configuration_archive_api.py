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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_plugin_configuration_archive import FlexV1PluginConfigurationArchive
from ..server.server import Server


class FlexV1PluginConfigurationArchiveApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginConfigurationArchiveApiWithRawResponse(client, server, auth)

    def update_plugin_configuration_archive(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginConfigurationArchive:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_plugin_configuration_archive(
            sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginConfigurationArchiveApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginConfigurationArchiveApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginConfigurationArchiveApiWithRawResponse(client, server, auth)

    async def update_plugin_configuration_archive(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginConfigurationArchive:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_plugin_configuration_archive(
                sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginConfigurationArchiveApiWithRawResponse:
        return self._with_raw_response


class FlexV1PluginConfigurationArchiveApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_plugin_configuration_archive(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginConfigurationArchive, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Configurations/{Sid}/Archive"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfigurationArchive],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginConfigurationArchiveApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def update_plugin_configuration_archive(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginConfigurationArchive, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin Configuration resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Configurations/{Sid}/Archive"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginConfigurationArchive],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
