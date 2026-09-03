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
from ..models.insights_v1_video_room_summary_video_participant_summary import (
    InsightsV1VideoRoomSummaryVideoParticipantSummary,
)
from ..models.list_video_participant_summary_response import ListVideoParticipantSummaryResponse
from ..server.server import Server


class InsightsV1Participant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1ParticipantWithRawResponse(client, server, auth)

    def fetch_video_participant_summary(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1VideoRoomSummaryVideoParticipantSummary:
        """Get Video Log Analyzer data for a Room Participant.

        Args:
            room_sid: The SID of the Room resource.
            participant_sid: The SID of the Participant resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_video_participant_summary(
            room_sid, participant_sid, request_options=request_options
        ).unwrap()

    def list_video_participant_summary(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVideoParticipantSummaryResponse:
        """Get a list of room participants.

        Args:
            room_sid: The SID of the Room resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_video_participant_summary(
            room_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1ParticipantWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1Participant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1ParticipantWithRawResponse(client, server, auth)

    async def fetch_video_participant_summary(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1VideoRoomSummaryVideoParticipantSummary:
        """Get Video Log Analyzer data for a Room Participant.

        Args:
            room_sid: The SID of the Room resource.
            participant_sid: The SID of the Participant resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_video_participant_summary(
                room_sid, participant_sid, request_options=request_options
            )
        ).unwrap()

    async def list_video_participant_summary(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVideoParticipantSummaryResponse:
        """Get a list of room participants.

        Args:
            room_sid: The SID of the Room resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_video_participant_summary(
                room_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1ParticipantWithRawResponse:
        return self._with_raw_response


class InsightsV1ParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_video_participant_summary(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1VideoRoomSummaryVideoParticipantSummary, RawError]:
        """Get Video Log Analyzer data for a Room Participant.

        Args:
            room_sid: The SID of the Room resource.
            participant_sid: The SID of the Participant resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}/Participants/{ParticipantSid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1VideoRoomSummaryVideoParticipantSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_video_participant_summary(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVideoParticipantSummaryResponse, RawError]:
        """Get a list of room participants.

        Args:
            room_sid: The SID of the Room resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}/Participants"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVideoParticipantSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1ParticipantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_video_participant_summary(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1VideoRoomSummaryVideoParticipantSummary, RawError]:
        """Get Video Log Analyzer data for a Room Participant.

        Args:
            room_sid: The SID of the Room resource.
            participant_sid: The SID of the Participant resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}/Participants/{ParticipantSid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1VideoRoomSummaryVideoParticipantSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_video_participant_summary(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVideoParticipantSummaryResponse, RawError]:
        """Get a list of room participants.

        Args:
            room_sid: The SID of the Room resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Video/Rooms/{RoomSid}/Participants"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVideoParticipantSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
