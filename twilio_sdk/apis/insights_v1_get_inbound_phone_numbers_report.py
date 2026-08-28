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
    param,
    raw_error_response,
)
from ..models.list_inbound_phone_numbers_reports import ListInboundPhoneNumbersReports
from ..server.server import Server


class InsightsV1GetInboundPhoneNumbersReport:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1GetInboundPhoneNumbersReportWithRawResponse(client, server, auth)

    def list_inbound_phone_numbers_report(
        self,
        report_id: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPhoneNumbersReports:
        """Get Inbound Phone Numbers Level Reports for the given Report Id.

        Args:
            report_id: A unique Report Id.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_inbound_phone_numbers_report(
            report_id, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1GetInboundPhoneNumbersReportWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1GetInboundPhoneNumbersReport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1GetInboundPhoneNumbersReportWithRawResponse(client, server, auth)

    async def list_inbound_phone_numbers_report(
        self,
        report_id: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPhoneNumbersReports:
        """Get Inbound Phone Numbers Level Reports for the given Report Id.

        Args:
            report_id: A unique Report Id.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_inbound_phone_numbers_report(
                report_id, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1GetInboundPhoneNumbersReportWithRawResponse:
        return self._with_raw_response


class InsightsV1GetInboundPhoneNumbersReportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_inbound_phone_numbers_report(
        self,
        report_id: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPhoneNumbersReports, RawError]:
        """Get Inbound Phone Numbers Level Reports for the given Report Id.

        Args:
            report_id: A unique Report Id.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v2/Voice/Reports/PhoneNumbers/Inbound/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInboundPhoneNumbersReports],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1GetInboundPhoneNumbersReportWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list_inbound_phone_numbers_report(
        self,
        report_id: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPhoneNumbersReports, RawError]:
        """Get Inbound Phone Numbers Level Reports for the given Report Id.

        Args:
            report_id: A unique Report Id.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v2/Voice/Reports/PhoneNumbers/Inbound/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInboundPhoneNumbersReports],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
