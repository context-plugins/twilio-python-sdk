from __future__ import annotations

from typing import Any

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
from ..models.video_v1_room_room_recording_rule import VideoV1RoomRoomRecordingRule
from ..server.server import Server


class VideoV1RecordingRules:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1RecordingRulesWithRawResponse(client, server, auth)

    def fetch_room_recording_rule(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecordingRule:
        """Returns a list of Recording Rules for the Room.

        Args:
            room_sid: The SID of the Room resource where the recording rules to fetch apply.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_recording_rule(room_sid, request_options=request_options).unwrap()

    def update_room_recording_rule(
        self, room_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecordingRule:
        """Update the Recording Rules for the Room

        Args:
            room_sid: The SID of the Room resource where the recording rules to update apply.
            rules: A JSON-encoded array of recording rules.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room_recording_rule(
            room_sid, rules=rules, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1RecordingRulesWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1RecordingRules:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1RecordingRulesWithRawResponse(client, server, auth)

    async def fetch_room_recording_rule(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecordingRule:
        """Returns a list of Recording Rules for the Room.

        Args:
            room_sid: The SID of the Room resource where the recording rules to fetch apply.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_recording_rule(room_sid, request_options=request_options)
        ).unwrap()

    async def update_room_recording_rule(
        self, room_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecordingRule:
        """Update the Recording Rules for the Room

        Args:
            room_sid: The SID of the Room resource where the recording rules to update apply.
            rules: A JSON-encoded array of recording rules.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_room_recording_rule(
                room_sid, rules=rules, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1RecordingRulesWithRawResponse:
        return self._with_raw_response


class VideoV1RecordingRulesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_room_recording_rule(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecordingRule, RawError]:
        """Returns a list of Recording Rules for the Room.

        Args:
            room_sid: The SID of the Room resource where the recording rules to fetch apply.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/RecordingRules"),
            path_params=[param[str]("RoomSid", room_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecordingRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_room_recording_rule(
        self, room_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecordingRule, RawError]:
        """Update the Recording Rules for the Room

        Args:
            room_sid: The SID of the Room resource where the recording rules to update apply.
            rules: A JSON-encoded array of recording rules.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/RecordingRules"),
            path_params=[param[str]("RoomSid", room_sid)],
            body=form_body([param[Any | None]("Rules", rules)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecordingRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1RecordingRulesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_room_recording_rule(
        self, room_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecordingRule, RawError]:
        """Returns a list of Recording Rules for the Room.

        Args:
            room_sid: The SID of the Room resource where the recording rules to fetch apply.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/RecordingRules"),
            path_params=[param[str]("RoomSid", room_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecordingRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_room_recording_rule(
        self, room_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecordingRule, RawError]:
        """Update the Recording Rules for the Room

        Args:
            room_sid: The SID of the Room resource where the recording rules to update apply.
            rules: A JSON-encoded array of recording rules.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/RecordingRules"),
            path_params=[param[str]("RoomSid", room_sid)],
            body=form_body([param[Any | None]("Rules", rules)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecordingRule],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
