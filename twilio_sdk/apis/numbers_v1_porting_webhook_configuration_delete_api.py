from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    param,
    raw_error_response,
)
from ..models.enums.porting_webhook_configuration_delete_enum_webhook_type import (
    PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
)
from ..server.server import Server


class NumbersV1PortingWebhookConfigurationDeleteApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse(client, server, auth)

    def delete_porting_webhook_configuration_delete(
        self,
        webhook_type: PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Allows the client to delete a webhook configuration.

        Args:
            webhook_type: The webhook type for the configuration to be delete. ``PORT_IN``, ``PORT_OUT``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_porting_webhook_configuration_delete(
            webhook_type, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingWebhookConfigurationDeleteApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse(
            client, server, auth
        )

    async def delete_porting_webhook_configuration_delete(
        self,
        webhook_type: PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Allows the client to delete a webhook configuration.

        Args:
            webhook_type: The webhook type for the configuration to be delete. ``PORT_IN``, ``PORT_OUT``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_porting_webhook_configuration_delete(
                webhook_type, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_porting_webhook_configuration_delete(
        self,
        webhook_type: PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Allows the client to delete a webhook configuration.

        Args:
            webhook_type: The webhook type for the configuration to be delete. ``PORT_IN``, ``PORT_OUT``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook/{WebhookType}"),
            path_params=[param[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr]("WebhookType", webhook_type)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingWebhookConfigurationDeleteApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def delete_porting_webhook_configuration_delete(
        self,
        webhook_type: PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Allows the client to delete a webhook configuration.

        Args:
            webhook_type: The webhook type for the configuration to be delete. ``PORT_IN``, ``PORT_OUT``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/Configuration/Webhook/{WebhookType}"),
            path_params=[param[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr]("WebhookType", webhook_type)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
