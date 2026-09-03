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
from ..models.flex_v1_plugin_version_archive import FlexV1PluginVersionArchive
from ..server.server import Server


class FlexV1PluginVersionArchiveApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginVersionArchiveApiWithRawResponse(client, server, auth)

    def update_plugin_version_archive(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginVersionArchive:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_plugin_version_archive(
            plugin_sid, sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginVersionArchiveApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginVersionArchiveApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginVersionArchiveApiWithRawResponse(client, server, auth)

    async def update_plugin_version_archive(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginVersionArchive:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_plugin_version_archive(
                plugin_sid, sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginVersionArchiveApiWithRawResponse:
        return self._with_raw_response


class FlexV1PluginVersionArchiveApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_plugin_version_archive(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginVersionArchive, RawError]:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}/Archive"),
            path_params=[param[str]("PluginSid", plugin_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginVersionArchive],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginVersionArchiveApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def update_plugin_version_archive(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginVersionArchive, RawError]:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to archive.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}/Archive"),
            path_params=[param[str]("PluginSid", plugin_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginVersionArchive],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
