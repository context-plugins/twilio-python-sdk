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
from ..models.flex_v1_provisioning_status import FlexV1ProvisioningStatus
from ..server.server import Server


class FlexV1ProvisioningStatusApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1ProvisioningStatusApiWithRawResponse(client, server, auth)

    def fetch_provisioning_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1ProvisioningStatus:
        """Status for email provisioning

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_provisioning_status(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> FlexV1ProvisioningStatusApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1ProvisioningStatusApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1ProvisioningStatusApiWithRawResponse(client, server, auth)

    async def fetch_provisioning_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1ProvisioningStatus:
        """Status for email provisioning

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_provisioning_status(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1ProvisioningStatusApiWithRawResponse:
        return self._with_raw_response


class FlexV1ProvisioningStatusApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_provisioning_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1ProvisioningStatus, RawError]:
        """Status for email provisioning

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/account/provision/status"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1ProvisioningStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1ProvisioningStatusApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_provisioning_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1ProvisioningStatus, RawError]:
        """Status for email provisioning

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/account/provision/status"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1ProvisioningStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
