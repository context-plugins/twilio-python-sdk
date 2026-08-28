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
from ..models.enums.metric_enum_stream_direction import MetricEnumStreamDirectionOrStr
from ..models.enums.metric_enum_twilio_edge import MetricEnumTwilioEdgeOrStr
from ..models.list_metric_response import ListMetricResponse
from ..server.server import Server


class InsightsV1Metric:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1MetricWithRawResponse(client, server, auth)

    def list_metric(
        self,
        call_sid: str,
        *,
        edge: MetricEnumTwilioEdgeOrStr | None = None,
        direction: MetricEnumStreamDirectionOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMetricResponse:
        """Get a list of Call Metrics for a Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            edge: The Edge of this Metric. One of ``unknown_edge``, ``carrier_edge``, ``sip_edge``, ``sdk_edge`` or
                ``client_edge``.
            direction: The Direction of this Metric. One of ``unknown``, ``inbound``, ``outbound`` or ``both``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_metric(
            call_sid,
            edge=edge,
            direction=direction,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1MetricWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1Metric:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1MetricWithRawResponse(client, server, auth)

    async def list_metric(
        self,
        call_sid: str,
        *,
        edge: MetricEnumTwilioEdgeOrStr | None = None,
        direction: MetricEnumStreamDirectionOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMetricResponse:
        """Get a list of Call Metrics for a Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            edge: The Edge of this Metric. One of ``unknown_edge``, ``carrier_edge``, ``sip_edge``, ``sdk_edge`` or
                ``client_edge``.
            direction: The Direction of this Metric. One of ``unknown``, ``inbound``, ``outbound`` or ``both``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_metric(
                call_sid,
                edge=edge,
                direction=direction,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1MetricWithRawResponse:
        return self._with_raw_response


class InsightsV1MetricWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_metric(
        self,
        call_sid: str,
        *,
        edge: MetricEnumTwilioEdgeOrStr | None = None,
        direction: MetricEnumStreamDirectionOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMetricResponse, RawError]:
        """Get a list of Call Metrics for a Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            edge: The Edge of this Metric. One of ``unknown_edge``, ``carrier_edge``, ``sip_edge``, ``sdk_edge`` or
                ``client_edge``.
            direction: The Direction of this Metric. One of ``unknown``, ``inbound``, ``outbound`` or ``both``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Metrics"),
            path_params=[param[str]("CallSid", call_sid)],
            query_params=[
                param[MetricEnumTwilioEdgeOrStr | None]("Edge", edge),
                param[MetricEnumStreamDirectionOrStr | None]("Direction", direction),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMetricResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1MetricWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_metric(
        self,
        call_sid: str,
        *,
        edge: MetricEnumTwilioEdgeOrStr | None = None,
        direction: MetricEnumStreamDirectionOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMetricResponse, RawError]:
        """Get a list of Call Metrics for a Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            edge: The Edge of this Metric. One of ``unknown_edge``, ``carrier_edge``, ``sip_edge``, ``sdk_edge`` or
                ``client_edge``.
            direction: The Direction of this Metric. One of ``unknown``, ``inbound``, ``outbound`` or ``both``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Metrics"),
            path_params=[param[str]("CallSid", call_sid)],
            query_params=[
                param[MetricEnumTwilioEdgeOrStr | None]("Edge", edge),
                param[MetricEnumStreamDirectionOrStr | None]("Direction", direction),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMetricResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
