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
    raw_error_response,
)
from ..models.numbers_v1_porting_webhook_configuration import NumbersV1PortingWebhookConfiguration
from ..server.server import Server


class NumbersV1PortingWebhookConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingWebhookConfigurationApiWithRawResponse(client, server, auth)

    def create_porting_webhook_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingWebhookConfiguration:
        """Create a Webhook Configuration

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_porting_webhook_configuration(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingWebhookConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingWebhookConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingWebhookConfigurationApiWithRawResponse(client, server, auth)

    async def create_porting_webhook_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingWebhookConfiguration:
        """Create a Webhook Configuration

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_porting_webhook_configuration(
                body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingWebhookConfigurationApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingWebhookConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_porting_webhook_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingWebhookConfiguration, RawError]:
        """Create a Webhook Configuration

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingWebhookConfigurationApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_porting_webhook_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingWebhookConfiguration, RawError]:
        """Create a Webhook Configuration

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
