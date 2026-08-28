from __future__ import annotations

from typing import Any

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_configuration import FlexV1Configuration
from ..server.server import Server


class FlexV1ConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1ConfigurationApiWithRawResponse(client, server, auth)

    def fetch_configuration3(
        self, *, ui_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Configuration:
        """Configuration for a Flex instance

        Args:
            ui_version: The Pinned UI version of the Configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_configuration3(
            ui_version=ui_version, request_options=request_options
        ).unwrap()

    def update_configuration3(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Configuration:
        """Configuration for a Flex instance

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_configuration3(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> FlexV1ConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1ConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1ConfigurationApiWithRawResponse(client, server, auth)

    async def fetch_configuration3(
        self, *, ui_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Configuration:
        """Configuration for a Flex instance

        Args:
            ui_version: The Pinned UI version of the Configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_configuration3(ui_version=ui_version, request_options=request_options)
        ).unwrap()

    async def update_configuration3(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Configuration:
        """Configuration for a Flex instance

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_configuration3(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1ConfigurationApiWithRawResponse:
        return self._with_raw_response


class FlexV1ConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_configuration3(
        self, *, ui_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Configuration, RawError]:
        """Configuration for a Flex instance

        Args:
            ui_version: The Pinned UI version of the Configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Configuration"),
            query_params=[param[str | None]("UiVersion", ui_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_configuration3(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Configuration, RawError]:
        """Configuration for a Flex instance

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Configuration"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1ConfigurationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_configuration3(
        self, *, ui_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Configuration, RawError]:
        """Configuration for a Flex instance

        Args:
            ui_version: The Pinned UI version of the Configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Configuration"),
            query_params=[param[str | None]("UiVersion", ui_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_configuration3(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Configuration, RawError]:
        """Configuration for a Flex instance

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Configuration"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
