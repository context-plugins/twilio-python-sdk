from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

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
from ..models.list_signing_request_configuration_response import ListSigningRequestConfigurationResponse
from ..models.numbers_v1_signing_request_configuration import NumbersV1SigningRequestConfiguration
from ..server.server import Server


class NumbersV1SigningRequestConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1SigningRequestConfigurationApiWithRawResponse(client, server, auth)

    def create_signing_request_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1SigningRequestConfiguration:
        """Synchronous operation to insert or update a configuration for the customer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_signing_request_configuration(
            body=body, request_options=request_options
        ).unwrap()

    def list_signing_request_configuration(
        self,
        *,
        country: str | None = None,
        product: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSigningRequestConfigurationResponse:
        """Synchronous operation to retrieve configurations for the customer.

        Args:
            country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
            product: The product or service for which is requesting the signature, this is an optional field, Example:
                Porting, Hosting
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_signing_request_configuration(
            country=country,
            product=product,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1SigningRequestConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1SigningRequestConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1SigningRequestConfigurationApiWithRawResponse(client, server, auth)

    async def create_signing_request_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1SigningRequestConfiguration:
        """Synchronous operation to insert or update a configuration for the customer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_signing_request_configuration(
                body=body, request_options=request_options
            )
        ).unwrap()

    async def list_signing_request_configuration(
        self,
        *,
        country: str | None = None,
        product: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSigningRequestConfigurationResponse:
        """Synchronous operation to retrieve configurations for the customer.

        Args:
            country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
            product: The product or service for which is requesting the signature, this is an optional field, Example:
                Porting, Hosting
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_signing_request_configuration(
                country=country,
                product=product,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1SigningRequestConfigurationApiWithRawResponse:
        return self._with_raw_response


class NumbersV1SigningRequestConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_signing_request_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1SigningRequestConfiguration, RawError]:
        """Synchronous operation to insert or update a configuration for the customer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SigningRequest/Configuration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1SigningRequestConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_signing_request_configuration(
        self,
        *,
        country: str | None = None,
        product: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSigningRequestConfigurationResponse, RawError]:
        """Synchronous operation to retrieve configurations for the customer.

        Args:
            country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
            product: The product or service for which is requesting the signature, this is an optional field, Example:
                Porting, Hosting
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/SigningRequest/Configuration"),
            query_params=[
                param[str | None]("Country", country),
                param[str | None]("Product", product),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSigningRequestConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1SigningRequestConfigurationApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_signing_request_configuration(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1SigningRequestConfiguration, RawError]:
        """Synchronous operation to insert or update a configuration for the customer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SigningRequest/Configuration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1SigningRequestConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_signing_request_configuration(
        self,
        *,
        country: str | None = None,
        product: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSigningRequestConfigurationResponse, RawError]:
        """Synchronous operation to retrieve configurations for the customer.

        Args:
            country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
            product: The product or service for which is requesting the signature, this is an optional field, Example:
                Porting, Hosting
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/SigningRequest/Configuration"),
            query_params=[
                param[str | None]("Country", country),
                param[str | None]("Product", product),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSigningRequestConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
