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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_plugin_plugin_version import FlexV1PluginPluginVersion
from ..models.list_plugin_version_response import ListPluginVersionResponse
from ..server.server import Server


class FlexV1PluginVersions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginVersionsWithRawResponse(client, server, auth)

    def create_plugin_version(
        self,
        plugin_sid: str,
        version: str,
        plugin_url: str,
        *,
        flex_metadata: str | None = None,
        changelog: str | None = None,
        private: bool | None = None,
        cli_version: str | None = None,
        validate_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginPluginVersion:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            version: The Flex Plugin Version's version.
            plugin_url: The URL of the Flex Plugin Version bundle
            flex_metadata: The Flex-Metadata HTTP request header
            changelog: The changelog of the Flex Plugin Version.
            private: Whether this Flex Plugin Version requires authorization.
            cli_version: The version of Flex Plugins CLI used to create this plugin
            validate_status: The validation status of the plugin, indicating whether it has been validated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_plugin_version(
            plugin_sid,
            version,
            plugin_url,
            flex_metadata=flex_metadata,
            changelog=changelog,
            private=private,
            cli_version=cli_version,
            validate_status=validate_status,
            request_options=request_options,
        ).unwrap()

    def fetch_plugin_version(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginPluginVersion:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_plugin_version(
            plugin_sid, sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def list_plugin_version(
        self,
        plugin_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginVersionResponse:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_plugin_version(
            plugin_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            flex_metadata=flex_metadata,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginVersionsWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginVersions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginVersionsWithRawResponse(client, server, auth)

    async def create_plugin_version(
        self,
        plugin_sid: str,
        version: str,
        plugin_url: str,
        *,
        flex_metadata: str | None = None,
        changelog: str | None = None,
        private: bool | None = None,
        cli_version: str | None = None,
        validate_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginPluginVersion:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            version: The Flex Plugin Version's version.
            plugin_url: The URL of the Flex Plugin Version bundle
            flex_metadata: The Flex-Metadata HTTP request header
            changelog: The changelog of the Flex Plugin Version.
            private: Whether this Flex Plugin Version requires authorization.
            cli_version: The version of Flex Plugins CLI used to create this plugin
            validate_status: The validation status of the plugin, indicating whether it has been validated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_plugin_version(
                plugin_sid,
                version,
                plugin_url,
                flex_metadata=flex_metadata,
                changelog=changelog,
                private=private,
                cli_version=cli_version,
                validate_status=validate_status,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_plugin_version(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginPluginVersion:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_plugin_version(
                plugin_sid, sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def list_plugin_version(
        self,
        plugin_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginVersionResponse:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
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
            await self._with_raw_response.list_plugin_version(
                plugin_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                flex_metadata=flex_metadata,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginVersionsWithRawResponse:
        return self._with_raw_response


class FlexV1PluginVersionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_plugin_version(
        self,
        plugin_sid: str,
        version: str,
        plugin_url: str,
        *,
        flex_metadata: str | None = None,
        changelog: str | None = None,
        private: bool | None = None,
        cli_version: str | None = None,
        validate_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginPluginVersion, RawError]:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            version: The Flex Plugin Version's version.
            plugin_url: The URL of the Flex Plugin Version bundle
            flex_metadata: The Flex-Metadata HTTP request header
            changelog: The changelog of the Flex Plugin Version.
            private: Whether this Flex Plugin Version requires authorization.
            cli_version: The version of Flex Plugins CLI used to create this plugin
            validate_status: The validation status of the plugin, indicating whether it has been validated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions"),
            path_params=[param[str]("PluginSid", plugin_sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Version", version),
                    param[str]("PluginUrl", plugin_url),
                    param[str | None]("Changelog", changelog),
                    param[bool | None]("Private", private),
                    param[str | None]("CliVersion", cli_version),
                    param[str | None]("ValidateStatus", validate_status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginPluginVersion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_plugin_version(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginPluginVersion, RawError]:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}"),
            path_params=[param[str]("PluginSid", plugin_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginPluginVersion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_plugin_version(
        self,
        plugin_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginVersionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions"),
            path_params=[param[str]("PluginSid", plugin_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginVersionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginVersionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_plugin_version(
        self,
        plugin_sid: str,
        version: str,
        plugin_url: str,
        *,
        flex_metadata: str | None = None,
        changelog: str | None = None,
        private: bool | None = None,
        cli_version: str | None = None,
        validate_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginPluginVersion, RawError]:
        """Send a ``POST`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            version: The Flex Plugin Version's version.
            plugin_url: The URL of the Flex Plugin Version bundle
            flex_metadata: The Flex-Metadata HTTP request header
            changelog: The changelog of the Flex Plugin Version.
            private: Whether this Flex Plugin Version requires authorization.
            cli_version: The version of Flex Plugins CLI used to create this plugin
            validate_status: The validation status of the plugin, indicating whether it has been validated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions"),
            path_params=[param[str]("PluginSid", plugin_sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Version", version),
                    param[str]("PluginUrl", plugin_url),
                    param[str | None]("Changelog", changelog),
                    param[bool | None]("Private", private),
                    param[str | None]("CliVersion", cli_version),
                    param[str | None]("ValidateStatus", validate_status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginPluginVersion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_plugin_version(
        self,
        plugin_sid: str,
        sid: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginPluginVersion, RawError]:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            sid: The SID of the Flex Plugin Version resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}"),
            path_params=[param[str]("PluginSid", plugin_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginPluginVersion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_plugin_version(
        self,
        plugin_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginVersionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            plugin_sid: The SID of the Flex Plugin the resource to belongs to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{PluginSid}/Versions"),
            path_params=[param[str]("PluginSid", plugin_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginVersionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
