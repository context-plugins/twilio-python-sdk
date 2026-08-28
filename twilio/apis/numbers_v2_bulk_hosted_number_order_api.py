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
from ..models.numbers_v2_bulk_hosted_number_order import NumbersV2BulkHostedNumberOrder
from ..server.server import Server


class NumbersV2BulkHostedNumberOrderApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2BulkHostedNumberOrderApiWithRawResponse(client, server, auth)

    def create_bulk_hosted_number_order(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2BulkHostedNumberOrder:
        """Host multiple phone numbers on Twilio's platform.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bulk_hosted_number_order(
            body=body, request_options=request_options
        ).unwrap()

    def fetch_bulk_hosted_number_order(
        self,
        bulk_hosting_sid: str,
        *,
        order_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2BulkHostedNumberOrder:
        """Fetch a specific BulkHostedNumberOrder.

        Args:
            bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
            order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete
                list of order statuses, please check
                'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_bulk_hosted_number_order(
            bulk_hosting_sid, order_status=order_status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2BulkHostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2BulkHostedNumberOrderApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2BulkHostedNumberOrderApiWithRawResponse(client, server, auth)

    async def create_bulk_hosted_number_order(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2BulkHostedNumberOrder:
        """Host multiple phone numbers on Twilio's platform.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_bulk_hosted_number_order(body=body, request_options=request_options)
        ).unwrap()

    async def fetch_bulk_hosted_number_order(
        self,
        bulk_hosting_sid: str,
        *,
        order_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2BulkHostedNumberOrder:
        """Fetch a specific BulkHostedNumberOrder.

        Args:
            bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
            order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete
                list of order statuses, please check
                'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_bulk_hosted_number_order(
                bulk_hosting_sid, order_status=order_status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2BulkHostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class NumbersV2BulkHostedNumberOrderApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bulk_hosted_number_order(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2BulkHostedNumberOrder, RawError]:
        """Host multiple phone numbers on Twilio's platform.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders/Bulk"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BulkHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_bulk_hosted_number_order(
        self,
        bulk_hosting_sid: str,
        *,
        order_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2BulkHostedNumberOrder, RawError]:
        """Fetch a specific BulkHostedNumberOrder.

        Args:
            bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
            order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete
                list of order statuses, please check
                'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders/Bulk/{BulkHostingSid}"),
            path_params=[param[str]("BulkHostingSid", bulk_hosting_sid)],
            query_params=[param[str | None]("OrderStatus", order_status)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BulkHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2BulkHostedNumberOrderApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_bulk_hosted_number_order(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2BulkHostedNumberOrder, RawError]:
        """Host multiple phone numbers on Twilio's platform.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders/Bulk"),
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BulkHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_bulk_hosted_number_order(
        self,
        bulk_hosting_sid: str,
        *,
        order_status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2BulkHostedNumberOrder, RawError]:
        """Fetch a specific BulkHostedNumberOrder.

        Args:
            bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
            order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete
                list of order statuses, please check
                'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders/Bulk/{BulkHostingSid}"),
            path_params=[param[str]("BulkHostingSid", bulk_hosting_sid)],
            query_params=[param[str | None]("OrderStatus", order_status)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BulkHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
