from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.room_participant_enum_status import RoomParticipantEnumStatusOrStr
from ..models.list_room_participant_response import ListRoomParticipantResponse
from ..models.video_v1_room_room_participant import VideoV1RoomRoomParticipant
from ..server.server import Server


class VideoV1Participant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1ParticipantWithRawResponse(client, server, auth)

    def fetch_room_participant(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipant:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resource to fetch.
            sid: The SID of the RoomParticipant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_participant(room_sid, sid, request_options=request_options).unwrap()

    def list_room_participant(
        self,
        room_sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        identity: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomParticipantResponse:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resources to read.
            status: Read only the participants with this status. Can be: ``connected`` or ``disconnected``. For
                ``in-progress`` Rooms the default Status is ``connected``, for ``completed`` Rooms only ``disconnected``
                Participants are returned.
            identity: Read only the Participants with this `User
                <https://www.twilio.com/docs/chat/rest/user-resource>`__ ``identity`` value.
            date_created_after: Read only Participants that started after this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            date_created_before: Read only Participants that started before this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_room_participant(
            room_sid,
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_room_participant(
        self,
        room_sid: str,
        sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomParticipant:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            status: The status of the Participant. Can be: ``connected`` or ``disconnected``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room_participant(
            room_sid, sid, status=status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1ParticipantWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1Participant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1ParticipantWithRawResponse(client, server, auth)

    async def fetch_room_participant(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipant:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resource to fetch.
            sid: The SID of the RoomParticipant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_participant(room_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_room_participant(
        self,
        room_sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        identity: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomParticipantResponse:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resources to read.
            status: Read only the participants with this status. Can be: ``connected`` or ``disconnected``. For
                ``in-progress`` Rooms the default Status is ``connected``, for ``completed`` Rooms only ``disconnected``
                Participants are returned.
            identity: Read only the Participants with this `User
                <https://www.twilio.com/docs/chat/rest/user-resource>`__ ``identity`` value.
            date_created_after: Read only Participants that started after this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            date_created_before: Read only Participants that started before this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_room_participant(
                room_sid,
                status=status,
                identity=identity,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_room_participant(
        self,
        room_sid: str,
        sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomParticipant:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            status: The status of the Participant. Can be: ``connected`` or ``disconnected``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_room_participant(
                room_sid, sid, status=status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1ParticipantWithRawResponse:
        return self._with_raw_response


class VideoV1ParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_room_participant(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipant, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resource to fetch.
            sid: The SID of the RoomParticipant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_room_participant(
        self,
        room_sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        identity: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomParticipantResponse, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resources to read.
            status: Read only the participants with this status. Can be: ``connected`` or ``disconnected``. For
                ``in-progress`` Rooms the default Status is ``connected``, for ``completed`` Rooms only ``disconnected``
                Participants are returned.
            identity: Read only the Participants with this `User
                <https://www.twilio.com/docs/chat/rest/user-resource>`__ ``identity`` value.
            date_created_after: Read only Participants that started after this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            date_created_before: Read only Participants that started before this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[RoomParticipantEnumStatusOrStr | None]("Status", status),
                param[str | None]("Identity", identity),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_room_participant(
        self,
        room_sid: str,
        sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomParticipant, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            status: The status of the Participant. Can be: ``connected`` or ``disconnected``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[RoomParticipantEnumStatusOrStr | None]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1ParticipantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_room_participant(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipant, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resource to fetch.
            sid: The SID of the RoomParticipant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_room_participant(
        self,
        room_sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        identity: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomParticipantResponse, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the Participant resources to read.
            status: Read only the participants with this status. Can be: ``connected`` or ``disconnected``. For
                ``in-progress`` Rooms the default Status is ``connected``, for ``completed`` Rooms only ``disconnected``
                Participants are returned.
            identity: Read only the Participants with this `User
                <https://www.twilio.com/docs/chat/rest/user-resource>`__ ``identity`` value.
            date_created_after: Read only Participants that started after this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            date_created_before: Read only Participants that started before this date in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[RoomParticipantEnumStatusOrStr | None]("Status", status),
                param[str | None]("Identity", identity),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_room_participant(
        self,
        room_sid: str,
        sid: str,
        *,
        status: RoomParticipantEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomParticipant, RawError]:
        """Participants in video rooms

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            status: The status of the Participant. Can be: ``connected`` or ``disconnected``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[RoomParticipantEnumStatusOrStr | None]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
