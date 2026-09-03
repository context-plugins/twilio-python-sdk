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
    raw_error_response,
)
from ..models.numbers_v1_porting_webhook_configuration_fetch import NumbersV1PortingWebhookConfigurationFetch
from ..server.server import Server


class NumbersV1PortingWebhookConfigurationFetchApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingWebhookConfigurationFetchApiWithRawResponse(client, server, auth)

    def fetch_porting_webhook_configuration_fetch(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingWebhookConfigurationFetch:
        """Allows to fetch the webhook configuration

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_porting_webhook_configuration_fetch(
            request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingWebhookConfigurationFetchApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingWebhookConfigurationFetchApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingWebhookConfigurationFetchApiWithRawResponse(client, server, auth)

    async def fetch_porting_webhook_configuration_fetch(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingWebhookConfigurationFetch:
        """Allows to fetch the webhook configuration

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_porting_webhook_configuration_fetch(request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingWebhookConfigurationFetchApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingWebhookConfigurationFetchApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_porting_webhook_configuration_fetch(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingWebhookConfigurationFetch, RawError]:
        """Allows to fetch the webhook configuration

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingWebhookConfigurationFetch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingWebhookConfigurationFetchApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_porting_webhook_configuration_fetch(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingWebhookConfigurationFetch, RawError]:
        """Allows to fetch the webhook configuration

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingWebhookConfigurationFetch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
