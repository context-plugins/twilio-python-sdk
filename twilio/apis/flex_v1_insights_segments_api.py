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
from ..models.list_insights_segments_response import ListInsightsSegmentsResponse
from ..server.server import Server


class FlexV1InsightsSegmentsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsSegmentsApiWithRawResponse(client, server, auth)

    def list_insights_segments(
        self,
        *,
        segment_id: str | None = None,
        reservation_id: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsSegmentsResponse:
        """To get segments for given reservation Ids

        Args:
            segment_id: To unique id of the segment
            reservation_id: The list of reservation Ids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_segments(
            segment_id=segment_id,
            reservation_id=reservation_id,
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsSegmentsApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsSegmentsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsSegmentsApiWithRawResponse(client, server, auth)

    async def list_insights_segments(
        self,
        *,
        segment_id: str | None = None,
        reservation_id: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsSegmentsResponse:
        """To get segments for given reservation Ids

        Args:
            segment_id: To unique id of the segment
            reservation_id: The list of reservation Ids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_insights_segments(
                segment_id=segment_id,
                reservation_id=reservation_id,
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsSegmentsApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsSegmentsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_insights_segments(
        self,
        *,
        segment_id: str | None = None,
        reservation_id: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsSegmentsResponse, RawError]:
        """To get segments for given reservation Ids

        Args:
            segment_id: To unique id of the segment
            reservation_id: The list of reservation Ids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/Segments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[list[str] | None]("ReservationId", reservation_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsSegmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsSegmentsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_insights_segments(
        self,
        *,
        segment_id: str | None = None,
        reservation_id: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsSegmentsResponse, RawError]:
        """To get segments for given reservation Ids

        Args:
            segment_id: To unique id of the segment
            reservation_id: The list of reservation Ids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/Segments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[list[str] | None]("ReservationId", reservation_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsSegmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
