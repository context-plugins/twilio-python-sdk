from __future__ import annotations

from typing import Any

from pydantic import AnyUrl

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
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.recording_transcription_enum_status import RecordingTranscriptionEnumStatusOrStr
from ..models.enums.room_enum_room_type import RoomEnumRoomTypeOrStr
from ..models.enums.room_enum_video_codec import RoomEnumVideoCodecOrStr
from ..models.list_room_response import ListRoomResponse
from ..models.video_v1_room import VideoV1Room
from ..server.server import Server


class VideoV1RoomApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1RoomApiWithRawResponse(client, server, auth)

    def create_room(
        self,
        *,
        enable_turn: bool | None = None,
        type_: RoomEnumRoomTypeOrStr | None = None,
        unique_name: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        max_participants: int | None = None,
        record_participants_on_connect: bool | None = None,
        transcribe_participants_on_connect: bool | None = None,
        video_codecs: list[RoomEnumVideoCodecOrStr] | None = None,
        media_region: str | None = None,
        recording_rules: Any | None = None,
        transcriptions_configuration: Any | None = None,
        audio_only: bool | None = None,
        max_participant_duration: int | None = None,
        empty_room_timeout: int | None = None,
        unused_room_timeout: int | None = None,
        large_room: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            enable_turn: Deprecated, now always considered to be true.
            type_: Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small``
                are deprecated.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as a
                ``room_sid`` in place of the resource's ``sid`` in the URL to address the resource, assuming it does not
                contain any `reserved characters <https://tools.ietf.org/html/rfc3986#section-2.2>`__ that would need to
                be URL encoded. This value is unique for ``in-progress`` rooms. SDK clients can use this name to connect
                to the room. REST API clients can use this name in place of the Room SID to interact with the room as
                long as the room is ``in-progress``.
            status_callback: The URL Twilio should call using the ``status_callback_method`` to send status information
                to your application on every room event. See `Status Callbacks
                <https://www.twilio.com/docs/video/api/status-callbacks>`__ for more info.
            status_callback_method: The HTTP method Twilio should use to call ``status_callback``. Can be ``POST`` or
                ``GET``.
            max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed
                value is 50.
            record_participants_on_connect: Whether to start recording when Participants connect.
            transcribe_participants_on_connect: Whether to start transcriptions when Participants connect. If
                TranscriptionsConfiguration is not provided, default settings will be used.
            video_codecs: An array of the video codecs that are supported when publishing a track in the room. Can be:
                ``VP8`` and ``H264``.
            media_region: The region for the Room's media server. Can be one of the `available Media Regions
                <https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers>`__.
            recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for
                recording
            transcriptions_configuration: A collection of properties that describe transcription behaviour. If
                TranscribeParticipantsOnConnect is set to true and TranscriptionsConfiguration is not provided, default
                settings will be used.
            audio_only: When set to true, indicates that the participants in the room will only publish audio. No video
                tracks will be allowed.
            max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The
                maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
            empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant
                leaves. Valid values range from 1 to 60 minutes (no fractions).
            unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid
                values range from 1 to 60 minutes (no fractions).
            large_room: When set to true, indicated that this is the large room.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_room(
            enable_turn=enable_turn,
            type_=type_,
            unique_name=unique_name,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            max_participants=max_participants,
            record_participants_on_connect=record_participants_on_connect,
            transcribe_participants_on_connect=transcribe_participants_on_connect,
            video_codecs=video_codecs,
            media_region=media_region,
            recording_rules=recording_rules,
            transcriptions_configuration=transcriptions_configuration,
            audio_only=audio_only,
            max_participant_duration=max_participant_duration,
            empty_room_timeout=empty_room_timeout,
            unused_room_timeout=unused_room_timeout,
            large_room=large_room,
            request_options=request_options,
        ).unwrap()

    def fetch_room(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room(sid, request_options=request_options).unwrap()

    def list_room(
        self,
        *,
        status: RecordingTranscriptionEnumStatusOrStr | None = None,
        unique_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomResponse:
        """Video rooms with one or more participants

        Args:
            status: Read only the rooms with this status. Can be: ``in-progress`` (default) or ``completed``
            unique_name: Read only rooms with the this ``unique_name``.
            date_created_after: Read only rooms that started on or after this date, given as ``YYYY-MM-DD``.
            date_created_before: Read only rooms that started before this date, given as ``YYYY-MM-DD``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_room(
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_room(
        self,
        sid: str,
        status: RecordingTranscriptionEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to update.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room(sid, status, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideoV1RoomApiWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1RoomApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1RoomApiWithRawResponse(client, server, auth)

    async def create_room(
        self,
        *,
        enable_turn: bool | None = None,
        type_: RoomEnumRoomTypeOrStr | None = None,
        unique_name: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        max_participants: int | None = None,
        record_participants_on_connect: bool | None = None,
        transcribe_participants_on_connect: bool | None = None,
        video_codecs: list[RoomEnumVideoCodecOrStr] | None = None,
        media_region: str | None = None,
        recording_rules: Any | None = None,
        transcriptions_configuration: Any | None = None,
        audio_only: bool | None = None,
        max_participant_duration: int | None = None,
        empty_room_timeout: int | None = None,
        unused_room_timeout: int | None = None,
        large_room: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            enable_turn: Deprecated, now always considered to be true.
            type_: Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small``
                are deprecated.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as a
                ``room_sid`` in place of the resource's ``sid`` in the URL to address the resource, assuming it does not
                contain any `reserved characters <https://tools.ietf.org/html/rfc3986#section-2.2>`__ that would need to
                be URL encoded. This value is unique for ``in-progress`` rooms. SDK clients can use this name to connect
                to the room. REST API clients can use this name in place of the Room SID to interact with the room as
                long as the room is ``in-progress``.
            status_callback: The URL Twilio should call using the ``status_callback_method`` to send status information
                to your application on every room event. See `Status Callbacks
                <https://www.twilio.com/docs/video/api/status-callbacks>`__ for more info.
            status_callback_method: The HTTP method Twilio should use to call ``status_callback``. Can be ``POST`` or
                ``GET``.
            max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed
                value is 50.
            record_participants_on_connect: Whether to start recording when Participants connect.
            transcribe_participants_on_connect: Whether to start transcriptions when Participants connect. If
                TranscriptionsConfiguration is not provided, default settings will be used.
            video_codecs: An array of the video codecs that are supported when publishing a track in the room. Can be:
                ``VP8`` and ``H264``.
            media_region: The region for the Room's media server. Can be one of the `available Media Regions
                <https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers>`__.
            recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for
                recording
            transcriptions_configuration: A collection of properties that describe transcription behaviour. If
                TranscribeParticipantsOnConnect is set to true and TranscriptionsConfiguration is not provided, default
                settings will be used.
            audio_only: When set to true, indicates that the participants in the room will only publish audio. No video
                tracks will be allowed.
            max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The
                maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
            empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant
                leaves. Valid values range from 1 to 60 minutes (no fractions).
            unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid
                values range from 1 to 60 minutes (no fractions).
            large_room: When set to true, indicated that this is the large room.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_room(
                enable_turn=enable_turn,
                type_=type_,
                unique_name=unique_name,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                max_participants=max_participants,
                record_participants_on_connect=record_participants_on_connect,
                transcribe_participants_on_connect=transcribe_participants_on_connect,
                video_codecs=video_codecs,
                media_region=media_region,
                recording_rules=recording_rules,
                transcriptions_configuration=transcriptions_configuration,
                audio_only=audio_only,
                max_participant_duration=max_participant_duration,
                empty_room_timeout=empty_room_timeout,
                unused_room_timeout=unused_room_timeout,
                large_room=large_room,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_room(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_room(sid, request_options=request_options)).unwrap()

    async def list_room(
        self,
        *,
        status: RecordingTranscriptionEnumStatusOrStr | None = None,
        unique_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomResponse:
        """Video rooms with one or more participants

        Args:
            status: Read only the rooms with this status. Can be: ``in-progress`` (default) or ``completed``
            unique_name: Read only rooms with the this ``unique_name``.
            date_created_after: Read only rooms that started on or after this date, given as ``YYYY-MM-DD``.
            date_created_before: Read only rooms that started before this date, given as ``YYYY-MM-DD``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_room(
                status=status,
                unique_name=unique_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_room(
        self,
        sid: str,
        status: RecordingTranscriptionEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Room:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to update.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_room(sid, status, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1RoomApiWithRawResponse:
        return self._with_raw_response


class VideoV1RoomApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_room(
        self,
        *,
        enable_turn: bool | None = None,
        type_: RoomEnumRoomTypeOrStr | None = None,
        unique_name: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        max_participants: int | None = None,
        record_participants_on_connect: bool | None = None,
        transcribe_participants_on_connect: bool | None = None,
        video_codecs: list[RoomEnumVideoCodecOrStr] | None = None,
        media_region: str | None = None,
        recording_rules: Any | None = None,
        transcriptions_configuration: Any | None = None,
        audio_only: bool | None = None,
        max_participant_duration: int | None = None,
        empty_room_timeout: int | None = None,
        unused_room_timeout: int | None = None,
        large_room: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            enable_turn: Deprecated, now always considered to be true.
            type_: Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small``
                are deprecated.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as a
                ``room_sid`` in place of the resource's ``sid`` in the URL to address the resource, assuming it does not
                contain any `reserved characters <https://tools.ietf.org/html/rfc3986#section-2.2>`__ that would need to
                be URL encoded. This value is unique for ``in-progress`` rooms. SDK clients can use this name to connect
                to the room. REST API clients can use this name in place of the Room SID to interact with the room as
                long as the room is ``in-progress``.
            status_callback: The URL Twilio should call using the ``status_callback_method`` to send status information
                to your application on every room event. See `Status Callbacks
                <https://www.twilio.com/docs/video/api/status-callbacks>`__ for more info.
            status_callback_method: The HTTP method Twilio should use to call ``status_callback``. Can be ``POST`` or
                ``GET``.
            max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed
                value is 50.
            record_participants_on_connect: Whether to start recording when Participants connect.
            transcribe_participants_on_connect: Whether to start transcriptions when Participants connect. If
                TranscriptionsConfiguration is not provided, default settings will be used.
            video_codecs: An array of the video codecs that are supported when publishing a track in the room. Can be:
                ``VP8`` and ``H264``.
            media_region: The region for the Room's media server. Can be one of the `available Media Regions
                <https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers>`__.
            recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for
                recording
            transcriptions_configuration: A collection of properties that describe transcription behaviour. If
                TranscribeParticipantsOnConnect is set to true and TranscriptionsConfiguration is not provided, default
                settings will be used.
            audio_only: When set to true, indicates that the participants in the room will only publish audio. No video
                tracks will be allowed.
            max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The
                maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
            empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant
                leaves. Valid values range from 1 to 60 minutes (no fractions).
            unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid
                values range from 1 to 60 minutes (no fractions).
            large_room: When set to true, indicated that this is the large room.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms"),
            body=form_body(
                [
                    param[bool | None]("EnableTurn", enable_turn),
                    param[RoomEnumRoomTypeOrStr | None]("Type", type_),
                    param[str | None]("UniqueName", unique_name),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[int | None]("MaxParticipants", max_participants),
                    param[bool | None]("RecordParticipantsOnConnect", record_participants_on_connect),
                    param[bool | None]("TranscribeParticipantsOnConnect", transcribe_participants_on_connect),
                    param[list[RoomEnumVideoCodecOrStr] | None]("VideoCodecs", video_codecs),
                    param[str | None]("MediaRegion", media_region),
                    param[Any | None]("RecordingRules", recording_rules),
                    param[Any | None]("TranscriptionsConfiguration", transcriptions_configuration),
                    param[bool | None]("AudioOnly", audio_only),
                    param[int | None]("MaxParticipantDuration", max_participant_duration),
                    param[int | None]("EmptyRoomTimeout", empty_room_timeout),
                    param[int | None]("UnusedRoomTimeout", unused_room_timeout),
                    param[bool | None]("LargeRoom", large_room),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_room(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_room(
        self,
        *,
        status: RecordingTranscriptionEnumStatusOrStr | None = None,
        unique_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomResponse, RawError]:
        """Video rooms with one or more participants

        Args:
            status: Read only the rooms with this status. Can be: ``in-progress`` (default) or ``completed``
            unique_name: Read only rooms with the this ``unique_name``.
            date_created_after: Read only rooms that started on or after this date, given as ``YYYY-MM-DD``.
            date_created_before: Read only rooms that started before this date, given as ``YYYY-MM-DD``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms"),
            query_params=[
                param[RecordingTranscriptionEnumStatusOrStr | None]("Status", status),
                param[str | None]("UniqueName", unique_name),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_room(
        self,
        sid: str,
        status: RecordingTranscriptionEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to update.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body([param[RecordingTranscriptionEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1RoomApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_room(
        self,
        *,
        enable_turn: bool | None = None,
        type_: RoomEnumRoomTypeOrStr | None = None,
        unique_name: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        max_participants: int | None = None,
        record_participants_on_connect: bool | None = None,
        transcribe_participants_on_connect: bool | None = None,
        video_codecs: list[RoomEnumVideoCodecOrStr] | None = None,
        media_region: str | None = None,
        recording_rules: Any | None = None,
        transcriptions_configuration: Any | None = None,
        audio_only: bool | None = None,
        max_participant_duration: int | None = None,
        empty_room_timeout: int | None = None,
        unused_room_timeout: int | None = None,
        large_room: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            enable_turn: Deprecated, now always considered to be true.
            type_: Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small``
                are deprecated.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as a
                ``room_sid`` in place of the resource's ``sid`` in the URL to address the resource, assuming it does not
                contain any `reserved characters <https://tools.ietf.org/html/rfc3986#section-2.2>`__ that would need to
                be URL encoded. This value is unique for ``in-progress`` rooms. SDK clients can use this name to connect
                to the room. REST API clients can use this name in place of the Room SID to interact with the room as
                long as the room is ``in-progress``.
            status_callback: The URL Twilio should call using the ``status_callback_method`` to send status information
                to your application on every room event. See `Status Callbacks
                <https://www.twilio.com/docs/video/api/status-callbacks>`__ for more info.
            status_callback_method: The HTTP method Twilio should use to call ``status_callback``. Can be ``POST`` or
                ``GET``.
            max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed
                value is 50.
            record_participants_on_connect: Whether to start recording when Participants connect.
            transcribe_participants_on_connect: Whether to start transcriptions when Participants connect. If
                TranscriptionsConfiguration is not provided, default settings will be used.
            video_codecs: An array of the video codecs that are supported when publishing a track in the room. Can be:
                ``VP8`` and ``H264``.
            media_region: The region for the Room's media server. Can be one of the `available Media Regions
                <https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers>`__.
            recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for
                recording
            transcriptions_configuration: A collection of properties that describe transcription behaviour. If
                TranscribeParticipantsOnConnect is set to true and TranscriptionsConfiguration is not provided, default
                settings will be used.
            audio_only: When set to true, indicates that the participants in the room will only publish audio. No video
                tracks will be allowed.
            max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The
                maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
            empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant
                leaves. Valid values range from 1 to 60 minutes (no fractions).
            unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid
                values range from 1 to 60 minutes (no fractions).
            large_room: When set to true, indicated that this is the large room.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms"),
            body=form_body(
                [
                    param[bool | None]("EnableTurn", enable_turn),
                    param[RoomEnumRoomTypeOrStr | None]("Type", type_),
                    param[str | None]("UniqueName", unique_name),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[int | None]("MaxParticipants", max_participants),
                    param[bool | None]("RecordParticipantsOnConnect", record_participants_on_connect),
                    param[bool | None]("TranscribeParticipantsOnConnect", transcribe_participants_on_connect),
                    param[list[RoomEnumVideoCodecOrStr] | None]("VideoCodecs", video_codecs),
                    param[str | None]("MediaRegion", media_region),
                    param[Any | None]("RecordingRules", recording_rules),
                    param[Any | None]("TranscriptionsConfiguration", transcriptions_configuration),
                    param[bool | None]("AudioOnly", audio_only),
                    param[int | None]("MaxParticipantDuration", max_participant_duration),
                    param[int | None]("EmptyRoomTimeout", empty_room_timeout),
                    param[int | None]("UnusedRoomTimeout", unused_room_timeout),
                    param[bool | None]("LargeRoom", large_room),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_room(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_room(
        self,
        *,
        status: RecordingTranscriptionEnumStatusOrStr | None = None,
        unique_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomResponse, RawError]:
        """Video rooms with one or more participants

        Args:
            status: Read only the rooms with this status. Can be: ``in-progress`` (default) or ``completed``
            unique_name: Read only rooms with the this ``unique_name``.
            date_created_after: Read only rooms that started on or after this date, given as ``YYYY-MM-DD``.
            date_created_before: Read only rooms that started before this date, given as ``YYYY-MM-DD``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms"),
            query_params=[
                param[RecordingTranscriptionEnumStatusOrStr | None]("Status", status),
                param[str | None]("UniqueName", unique_name),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_room(
        self,
        sid: str,
        status: RecordingTranscriptionEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Room, RawError]:
        """Video rooms with one or more participants

        Args:
            sid: The SID of the Room resource to update.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body([param[RecordingTranscriptionEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Room],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
