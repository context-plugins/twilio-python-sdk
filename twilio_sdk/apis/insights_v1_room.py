from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.video_room_summary_enum_codec import VideoRoomSummaryEnumCodecOrStr
from ..models.enums.video_room_summary_enum_room_type import VideoRoomSummaryEnumRoomTypeOrStr
from ..models.insights_v1_video_room_summary import InsightsV1VideoRoomSummary
from ..models.list_video_room_summary_response import ListVideoRoomSummaryResponse
from ..server.server import Server


class InsightsV1Room:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1RoomWithRawResponse(client, server, auth)

    def fetch_video_room_summary(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1VideoRoomSummary:
        """Get Video Log Analyzer data for a Room.

        Args:
            room_sid: The SID of the Room resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_video_room_summary(room_sid, request_options=request_options).unwrap()

    def list_video_room_summary(
        self,
        *,
        room_type: list[VideoRoomSummaryEnumRoomTypeOrStr] | None = None,
        codec: list[VideoRoomSummaryEnumCodecOrStr] | None = None,
        room_name: str | None = None,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVideoRoomSummaryResponse:
        """Get a list of Programmable Video Rooms.

        Args:
            room_type: Type of room. Can be ``go``, ``peer_to_peer``, ``group``, or ``group_small``.
            codec: Codecs used by participants in the room. Can be ``VP8``, ``H264``, or ``VP9``.
            room_name: Room friendly name.
            created_after: Only read rooms that started on or after this ISO 8601 timestamp.
            created_before: Only read rooms that started before this ISO 8601 timestamp.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_video_room_summary(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1RoomWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1Room:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1RoomWithRawResponse(client, server, auth)

    async def fetch_video_room_summary(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1VideoRoomSummary:
        """Get Video Log Analyzer data for a Room.

        Args:
            room_sid: The SID of the Room resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_video_room_summary(room_sid, request_options=request_options)
        ).unwrap()

    async def list_video_room_summary(
        self,
        *,
        room_type: list[VideoRoomSummaryEnumRoomTypeOrStr] | None = None,
        codec: list[VideoRoomSummaryEnumCodecOrStr] | None = None,
        room_name: str | None = None,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVideoRoomSummaryResponse:
        """Get a list of Programmable Video Rooms.

        Args:
            room_type: Type of room. Can be ``go``, ``peer_to_peer``, ``group``, or ``group_small``.
            codec: Codecs used by participants in the room. Can be ``VP8``, ``H264``, or ``VP9``.
            room_name: Room friendly name.
            created_after: Only read rooms that started on or after this ISO 8601 timestamp.
            created_before: Only read rooms that started before this ISO 8601 timestamp.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_video_room_summary(
                room_type=room_type,
                codec=codec,
                room_name=room_name,
                created_after=created_after,
                created_before=created_before,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1RoomWithRawResponse:
        return self._with_raw_response


class InsightsV1RoomWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_video_room_summary(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1VideoRoomSummary, RawError]:
        """Get Video Log Analyzer data for a Room.

        Args:
            room_sid: The SID of the Room resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}"),
            path_params=[param[str]("RoomSid", room_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1VideoRoomSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_video_room_summary(
        self,
        *,
        room_type: list[VideoRoomSummaryEnumRoomTypeOrStr] | None = None,
        codec: list[VideoRoomSummaryEnumCodecOrStr] | None = None,
        room_name: str | None = None,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVideoRoomSummaryResponse, RawError]:
        """Get a list of Programmable Video Rooms.

        Args:
            room_type: Type of room. Can be ``go``, ``peer_to_peer``, ``group``, or ``group_small``.
            codec: Codecs used by participants in the room. Can be ``VP8``, ``H264``, or ``VP9``.
            room_name: Room friendly name.
            created_after: Only read rooms that started on or after this ISO 8601 timestamp.
            created_before: Only read rooms that started before this ISO 8601 timestamp.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms"),
            query_params=[
                param[list[VideoRoomSummaryEnumRoomTypeOrStr] | None]("RoomType", room_type),
                param[list[VideoRoomSummaryEnumCodecOrStr] | None]("Codec", codec),
                param[str | None]("RoomName", room_name),
                param[RFC3339DateTime | None]("CreatedAfter", created_after),
                param[RFC3339DateTime | None]("CreatedBefore", created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVideoRoomSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1RoomWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_video_room_summary(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1VideoRoomSummary, RawError]:
        """Get Video Log Analyzer data for a Room.

        Args:
            room_sid: The SID of the Room resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}"),
            path_params=[param[str]("RoomSid", room_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1VideoRoomSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_video_room_summary(
        self,
        *,
        room_type: list[VideoRoomSummaryEnumRoomTypeOrStr] | None = None,
        codec: list[VideoRoomSummaryEnumCodecOrStr] | None = None,
        room_name: str | None = None,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVideoRoomSummaryResponse, RawError]:
        """Get a list of Programmable Video Rooms.

        Args:
            room_type: Type of room. Can be ``go``, ``peer_to_peer``, ``group``, or ``group_small``.
            codec: Codecs used by participants in the room. Can be ``VP8``, ``H264``, or ``VP9``.
            room_name: Room friendly name.
            created_after: Only read rooms that started on or after this ISO 8601 timestamp.
            created_before: Only read rooms that started before this ISO 8601 timestamp.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms"),
            query_params=[
                param[list[VideoRoomSummaryEnumRoomTypeOrStr] | None]("RoomType", room_type),
                param[list[VideoRoomSummaryEnumCodecOrStr] | None]("Codec", codec),
                param[str | None]("RoomName", room_name),
                param[RFC3339DateTime | None]("CreatedAfter", created_after),
                param[RFC3339DateTime | None]("CreatedBefore", created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVideoRoomSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
