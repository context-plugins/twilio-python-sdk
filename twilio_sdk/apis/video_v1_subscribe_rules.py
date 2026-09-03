from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.video_v1_room_room_participant_room_participant_subscribe_rule import (
    VideoV1RoomRoomParticipantRoomParticipantSubscribeRule,
)
from ..server.server import Server


class VideoV1SubscribeRules:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1SubscribeRulesWithRawResponse(client, server, auth)

    def fetch_room_participant_subscribe_rule(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule:
        """Returns a list of Subscribe Rules for the Participant.

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to fetch apply.
            participant_sid: The SID of the Participant resource with the subscribe rules to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_participant_subscribe_rule(
            room_sid, participant_sid, request_options=request_options
        ).unwrap()

    def update_room_participant_subscribe_rule(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        rules: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule:
        """Update the Subscribe Rules for the Participant

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to update apply.
            participant_sid: The SID of the Participant resource to update the Subscribe Rules.
            rules: A JSON-encoded array of subscribe rules. See the `Specifying Subscribe Rules
                <https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr>`__ section for further
                information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room_participant_subscribe_rule(
            room_sid, participant_sid, rules=rules, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1SubscribeRulesWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1SubscribeRules:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1SubscribeRulesWithRawResponse(client, server, auth)

    async def fetch_room_participant_subscribe_rule(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule:
        """Returns a list of Subscribe Rules for the Participant.

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to fetch apply.
            participant_sid: The SID of the Participant resource with the subscribe rules to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_participant_subscribe_rule(
                room_sid, participant_sid, request_options=request_options
            )
        ).unwrap()

    async def update_room_participant_subscribe_rule(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        rules: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule:
        """Update the Subscribe Rules for the Participant

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to update apply.
            participant_sid: The SID of the Participant resource to update the Subscribe Rules.
            rules: A JSON-encoded array of subscribe rules. See the `Specifying Subscribe Rules
                <https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr>`__ section for further
                information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_room_participant_subscribe_rule(
                room_sid, participant_sid, rules=rules, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1SubscribeRulesWithRawResponse:
        return self._with_raw_response


class VideoV1SubscribeRulesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_room_participant_subscribe_rule(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]:
        """Returns a list of Subscribe Rules for the Participant.

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to fetch apply.
            participant_sid: The SID of the Participant resource with the subscribe rules to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_room_participant_subscribe_rule(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        rules: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]:
        """Update the Subscribe Rules for the Participant

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to update apply.
            participant_sid: The SID of the Participant resource to update the Subscribe Rules.
            rules: A JSON-encoded array of subscribe rules. See the `Specifying Subscribe Rules
                <https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr>`__ section for further
                information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any | None]("Rules", rules)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1SubscribeRulesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_room_participant_subscribe_rule(
        self, room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]:
        """Returns a list of Subscribe Rules for the Participant.

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to fetch apply.
            participant_sid: The SID of the Participant resource with the subscribe rules to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_room_participant_subscribe_rule(
        self,
        room_sid: str,
        participant_sid: str,
        *,
        rules: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]:
        """Update the Subscribe Rules for the Participant

        Args:
            room_sid: The SID of the Room resource where the subscribe rules to update apply.
            participant_sid: The SID of the Participant resource to update the Subscribe Rules.
            rules: A JSON-encoded array of subscribe rules. See the `Specifying Subscribe Rules
                <https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr>`__ section for further
                information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("ParticipantSid", participant_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any | None]("Rules", rules)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
