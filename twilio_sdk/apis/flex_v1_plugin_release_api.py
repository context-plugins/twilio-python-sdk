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
from ..models.flex_v1_plugin_release import FlexV1PluginRelease
from ..models.list_plugin_release_response import ListPluginReleaseResponse
from ..server.server import Server


class FlexV1PluginReleaseApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginReleaseApiWithRawResponse(client, server, auth)

    def create_plugin_release(
        self,
        configuration_id: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginRelease:
        """Send a ``POST`` request.

        Args:
            configuration_id: The SID or the Version of the Flex Plugin Configuration to release.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_plugin_release(
            configuration_id, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def fetch_plugin_release(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginRelease:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Release resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_plugin_release(
            sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def list_plugin_release(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginReleaseResponse:
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
        return self._with_raw_response.list_plugin_release(
            page_size=page_size,
            page=page,
            page_token=page_token,
            flex_metadata=flex_metadata,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginReleaseApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginReleaseApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginReleaseApiWithRawResponse(client, server, auth)

    async def create_plugin_release(
        self,
        configuration_id: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1PluginRelease:
        """Send a ``POST`` request.

        Args:
            configuration_id: The SID or the Version of the Flex Plugin Configuration to release.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_plugin_release(
                configuration_id, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def fetch_plugin_release(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1PluginRelease:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Release resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_plugin_release(
                sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def list_plugin_release(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginReleaseResponse:
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
            await self._with_raw_response.list_plugin_release(
                page_size=page_size,
                page=page,
                page_token=page_token,
                flex_metadata=flex_metadata,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginReleaseApiWithRawResponse:
        return self._with_raw_response


class FlexV1PluginReleaseApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_plugin_release(
        self,
        configuration_id: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginRelease, RawError]:
        """Send a ``POST`` request.

        Args:
            configuration_id: The SID or the Version of the Flex Plugin Configuration to release.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Releases"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("ConfigurationId", configuration_id)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_plugin_release(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginRelease, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Release resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Releases/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_plugin_release(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginReleaseResponse, RawError]:
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
            url_template=self._server.default13("/v1/PluginService/Releases"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginReleaseResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginReleaseApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_plugin_release(
        self,
        configuration_id: str,
        *,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1PluginRelease, RawError]:
        """Send a ``POST`` request.

        Args:
            configuration_id: The SID or the Version of the Flex Plugin Configuration to release.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Releases"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("ConfigurationId", configuration_id)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_plugin_release(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1PluginRelease, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin Release resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Releases/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1PluginRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_plugin_release(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginReleaseResponse, RawError]:
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
            url_template=self._server.default13("/v1/PluginService/Releases"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginReleaseResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
