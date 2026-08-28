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
from ..models.list_room_participant_published_track_response import ListRoomParticipantPublishedTrackResponse
from ..models.video_v1_room_room_participant_room_participant_published_track import (
    VideoV1RoomRoomParticipantRoomParticipantPublishedTrack,
)
from ..server.server import Server


class VideoV1PublishedTrack:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1PublishedTrackWithRawResponse(client, server, auth)

    def fetch_room_participant_published_track(
        self, room_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantPublishedTrack:
        """Returns a single Track resource represented by TrackName or SID.

        Args:
            room_sid: The SID of the Room resource where the Track resource to fetch is published.
            participant_sid: The SID of the Participant resource with the published track to fetch.
            sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_participant_published_track(
            room_sid, participant_sid, sid, request_options=request_options
        ).unwrap()

    def list_room_participant_published_track(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomParticipantPublishedTrackResponse:
        """Returns a list of tracks associated with a given Participant. Only ``currently`` Published Tracks are in the
        list resource.

        Args:
            room_sid: The SID of the Room resource where the Track resources to read are published.
            participant_sid: The SID of the Participant resource with the published tracks to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_room_participant_published_track(
            room_sid,
            participant_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1PublishedTrackWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1PublishedTrack:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1PublishedTrackWithRawResponse(client, server, auth)

    async def fetch_room_participant_published_track(
        self, room_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantPublishedTrack:
        """Returns a single Track resource represented by TrackName or SID.

        Args:
            room_sid: The SID of the Room resource where the Track resource to fetch is published.
            participant_sid: The SID of the Participant resource with the published track to fetch.
            sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_participant_published_track(
                room_sid, participant_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_room_participant_published_track(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomParticipantPublishedTrackResponse:
        """Returns a list of tracks associated with a given Participant. Only ``currently`` Published Tracks are in the
        list resource.

        Args:
            room_sid: The SID of the Room resource where the Track resources to read are published.
            participant_sid: The SID of the Participant resource with the published tracks to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_room_participant_published_track(
                room_sid,
                participant_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1PublishedTrackWithRawResponse:
        return self._with_raw_response


class VideoV1PublishedTrackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_room_participant_published_track(
        self, room_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack, RawError]:
        """Returns a single Track resource represented by TrackName or SID.

        Args:
            room_sid: The SID of the Room resource where the Track resource to fetch is published.
            participant_sid: The SID of the Participant resource with the published track to fetch.
            sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6(
                "/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid}"
            ),
            path_params=[
                param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_room_participant_published_track(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomParticipantPublishedTrackResponse, RawError]:
        """Returns a list of tracks associated with a given Participant. Only ``currently`` Published Tracks are in the
        list resource.

        Args:
            room_sid: The SID of the Room resource where the Track resources to read are published.
            participant_sid: The SID of the Participant resource with the published tracks to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomParticipantPublishedTrackResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1PublishedTrackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_room_participant_published_track(
        self, room_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack, RawError]:
        """Returns a single Track resource represented by TrackName or SID.

        Args:
            room_sid: The SID of the Room resource where the Track resource to fetch is published.
            participant_sid: The SID of the Participant resource with the published track to fetch.
            sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6(
                "/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid}"
            ),
            path_params=[
                param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_room_participant_published_track(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomParticipantPublishedTrackResponse, RawError]:
        """Returns a list of tracks associated with a given Participant. Only ``currently`` Published Tracks are in the
        list resource.

        Args:
            room_sid: The SID of the Room resource where the Track resources to read are published.
            participant_sid: The SID of the Participant resource with the published tracks to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomParticipantPublishedTrackResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
