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
from ..models.video_v1_room_room_participant_room_participant_anonymize import (
    VideoV1RoomRoomParticipantRoomParticipantAnonymize,
)
from ..server.server import Server


class VideoV1Anonymize:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1AnonymizeWithRawResponse(client, server, auth)

    def update_room_participant_anonymize(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantAnonymize:
        """Send a ``POST`` request.

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room_participant_anonymize(
            room_sid, sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1AnonymizeWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1Anonymize:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1AnonymizeWithRawResponse(client, server, auth)

    async def update_room_participant_anonymize(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantAnonymize:
        """Send a ``POST`` request.

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_room_participant_anonymize(
                room_sid, sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1AnonymizeWithRawResponse:
        return self._with_raw_response


class VideoV1AnonymizeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_room_participant_anonymize(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantAnonymize, RawError]:
        """Send a ``POST`` request.

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantAnonymize],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1AnonymizeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def update_room_participant_anonymize(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantAnonymize, RawError]:
        """Send a ``POST`` request.

        Args:
            room_sid: The SID of the room with the participant to update.
            sid: The SID of the RoomParticipant resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantAnonymize],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
