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
from ..models.enums.summary_enum_processing_state import SummaryEnumProcessingStateOrStr
from ..models.insights_v1_call_summary import InsightsV1CallSummary
from ..server.server import Server


class InsightsV1CallSummaryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1CallSummaryApiWithRawResponse(client, server, auth)

    def fetch_summary(
        self,
        call_sid: str,
        *,
        processing_state: SummaryEnumProcessingStateOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1CallSummary:
        """Get a specific Call Summary.

        Args:
            call_sid: The unique SID identifier of the Call.
            processing_state: The Processing State of this Call Summary. One of ``complete``, ``partial`` or ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_summary(
            call_sid, processing_state=processing_state, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1CallSummaryApiWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1CallSummaryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1CallSummaryApiWithRawResponse(client, server, auth)

    async def fetch_summary(
        self,
        call_sid: str,
        *,
        processing_state: SummaryEnumProcessingStateOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1CallSummary:
        """Get a specific Call Summary.

        Args:
            call_sid: The unique SID identifier of the Call.
            processing_state: The Processing State of this Call Summary. One of ``complete``, ``partial`` or ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_summary(
                call_sid, processing_state=processing_state, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1CallSummaryApiWithRawResponse:
        return self._with_raw_response


class InsightsV1CallSummaryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_summary(
        self,
        call_sid: str,
        *,
        processing_state: SummaryEnumProcessingStateOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1CallSummary, RawError]:
        """Get a specific Call Summary.

        Args:
            call_sid: The unique SID identifier of the Call.
            processing_state: The Processing State of this Call Summary. One of ``complete``, ``partial`` or ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Summary"),
            path_params=[param[str]("CallSid", call_sid)],
            query_params=[param[SummaryEnumProcessingStateOrStr | None]("ProcessingState", processing_state)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1CallSummaryApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_summary(
        self,
        call_sid: str,
        *,
        processing_state: SummaryEnumProcessingStateOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1CallSummary, RawError]:
        """Get a specific Call Summary.

        Args:
            call_sid: The unique SID identifier of the Call.
            processing_state: The Processing State of this Call Summary. One of ``complete``, ``partial`` or ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Summary"),
            path_params=[param[str]("CallSid", call_sid)],
            query_params=[param[SummaryEnumProcessingStateOrStr | None]("ProcessingState", processing_state)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
