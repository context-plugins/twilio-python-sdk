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
from ..models.insights_v2_account_report import InsightsV2AccountReport
from ..server.server import Server


class InsightsV1GetAccountReport:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1GetAccountReportWithRawResponse(client, server, auth)

    def fetch_account_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV2AccountReport:
        """Get Account Level Report for the given Report Id.

        Args:
            report_id: A unique request id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_account_report(report_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1GetAccountReportWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1GetAccountReport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1GetAccountReportWithRawResponse(client, server, auth)

    async def fetch_account_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV2AccountReport:
        """Get Account Level Report for the given Report Id.

        Args:
            report_id: A unique request id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_account_report(report_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1GetAccountReportWithRawResponse:
        return self._with_raw_response


class InsightsV1GetAccountReportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_account_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV2AccountReport, RawError]:
        """Get Account Level Report for the given Report Id.

        Args:
            report_id: A unique request id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v2/Voice/Reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV2AccountReport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1GetAccountReportWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_account_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV2AccountReport, RawError]:
        """Get Account Level Report for the given Report Id.

        Args:
            report_id: A unique request id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v2/Voice/Reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV2AccountReport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
