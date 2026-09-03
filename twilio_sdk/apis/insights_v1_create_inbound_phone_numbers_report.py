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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.insights_v2_create_phone_numbers_report_request import (
    InsightsV2CreatePhoneNumbersReportRequest,
    InsightsV2CreatePhoneNumbersReportRequestDict,
)
from ..models.insights_v2_create_report_response import InsightsV2CreateReportResponse
from ..server.server import Server


class InsightsV1CreateInboundPhoneNumbersReport:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1CreateInboundPhoneNumbersReportWithRawResponse(client, server, auth)

    def create_inbound_phone_numbers_report(
        self,
        *,
        body: InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV2CreateReportResponse:
        """Create Inbound specific Phone Numbers Report for a specific account with given time range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_inbound_phone_numbers_report(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1CreateInboundPhoneNumbersReportWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1CreateInboundPhoneNumbersReport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1CreateInboundPhoneNumbersReportWithRawResponse(client, server, auth)

    async def create_inbound_phone_numbers_report(
        self,
        *,
        body: InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV2CreateReportResponse:
        """Create Inbound specific Phone Numbers Report for a specific account with given time range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_inbound_phone_numbers_report(
                body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1CreateInboundPhoneNumbersReportWithRawResponse:
        return self._with_raw_response


class InsightsV1CreateInboundPhoneNumbersReportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_inbound_phone_numbers_report(
        self,
        *,
        body: InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV2CreateReportResponse, RawError]:
        """Create Inbound specific Phone Numbers Report for a specific account with given time range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v2/Voice/Reports/PhoneNumbers/Inbound"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None
            ](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV2CreateReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1CreateInboundPhoneNumbersReportWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_inbound_phone_numbers_report(
        self,
        *,
        body: InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV2CreateReportResponse, RawError]:
        """Create Inbound specific Phone Numbers Report for a specific account with given time range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v2/Voice/Reports/PhoneNumbers/Inbound"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None
            ](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV2CreateReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
