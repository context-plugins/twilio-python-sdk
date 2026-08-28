from __future__ import annotations

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
from ..models.flex_v1_plugin import FlexV1Plugin
from ..models.list_plugin_response import ListPluginResponse
from ..server.server import Server


class FlexV1PluginApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1PluginApiWithRawResponse(client, server, auth)

    def create_plugin(
        self,
        unique_name: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Plugin:
        """Send a ``POST`` request.

        Args:
            unique_name: The Flex Plugin's unique name.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you create to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_plugin(
            unique_name,
            flex_metadata=flex_metadata,
            friendly_name=friendly_name,
            description=description,
            request_options=request_options,
        ).unwrap()

    def fetch_plugin(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Plugin:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_plugin(
            sid, flex_metadata=flex_metadata, request_options=request_options
        ).unwrap()

    def list_plugin(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginResponse:
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
        return self._with_raw_response.list_plugin(
            page_size=page_size,
            page=page,
            page_token=page_token,
            flex_metadata=flex_metadata,
            request_options=request_options,
        ).unwrap()

    def update_plugin(
        self,
        sid: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Plugin:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin resource to update.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you update to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_plugin(
            sid,
            flex_metadata=flex_metadata,
            friendly_name=friendly_name,
            description=description,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1PluginApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1PluginApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1PluginApiWithRawResponse(client, server, auth)

    async def create_plugin(
        self,
        unique_name: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Plugin:
        """Send a ``POST`` request.

        Args:
            unique_name: The Flex Plugin's unique name.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you create to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_plugin(
                unique_name,
                flex_metadata=flex_metadata,
                friendly_name=friendly_name,
                description=description,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_plugin(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Plugin:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_plugin(
                sid, flex_metadata=flex_metadata, request_options=request_options
            )
        ).unwrap()

    async def list_plugin(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPluginResponse:
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
            await self._with_raw_response.list_plugin(
                page_size=page_size,
                page=page,
                page_token=page_token,
                flex_metadata=flex_metadata,
                request_options=request_options,
            )
        ).unwrap()

    async def update_plugin(
        self,
        sid: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Plugin:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin resource to update.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you update to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_plugin(
                sid,
                flex_metadata=flex_metadata,
                friendly_name=friendly_name,
                description=description,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1PluginApiWithRawResponse:
        return self._with_raw_response


class FlexV1PluginApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_plugin(
        self,
        unique_name: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``POST`` request.

        Args:
            unique_name: The Flex Plugin's unique name.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you create to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            body=form_body(
                [
                    param[str]("UniqueName", unique_name),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_plugin(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_plugin(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginResponse, RawError]:
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
            url_template=self._server.default13("/v1/PluginService/Plugins"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_plugin(
        self,
        sid: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin resource to update.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you update to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[str | None]("Description", description)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1PluginApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_plugin(
        self,
        unique_name: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``POST`` request.

        Args:
            unique_name: The Flex Plugin's unique name.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you create to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins"),
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            body=form_body(
                [
                    param[str]("UniqueName", unique_name),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_plugin(
        self, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Flex Plugin resource to fetch.
            flex_metadata: The Flex-Metadata HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/PluginService/Plugins/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_plugin(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        flex_metadata: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPluginResponse, RawError]:
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
            url_template=self._server.default13("/v1/PluginService/Plugins"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPluginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_plugin(
        self,
        sid: str,
        *,
        flex_metadata: str | None = None,
        friendly_name: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Plugin, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Flex Plugin resource to update.
            flex_metadata: The Flex-Metadata HTTP request header
            friendly_name: The Flex Plugin's friendly name.
            description: A descriptive string that you update to describe the plugin resource. It can be up to 500
                characters long
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/PluginService/Plugins/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Flex-Metadata", flex_metadata)],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[str | None]("Description", description)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Plugin],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
