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
    empty_response,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.room_recording_enum_status import RoomRecordingEnumStatusOrStr
from ..models.list_room_recording_response import ListRoomRecordingResponse
from ..models.video_v1_room_room_recording import VideoV1RoomRoomRecording
from ..server.server import Server


class VideoV1RoomRecording:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1RoomRecordingWithRawResponse(client, server, auth)

    def delete_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resource to delete.
            sid: The SID of the RoomRecording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_room_recording(room_sid, sid, request_options=request_options).unwrap()

    def fetch_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecording:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the Room resource with the recording to fetch.
            sid: The SID of the RoomRecording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_recording(room_sid, sid, request_options=request_options).unwrap()

    def list_room_recording(
        self,
        room_sid: str,
        *,
        status: RoomRecordingEnumStatusOrStr | None = None,
        source_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomRecordingResponse:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resources to read.
            status: Read only the recordings with this status. Can be: ``processing``, ``completed``, or ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only Recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_room_recording(
            room_sid,
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1RoomRecordingWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1RoomRecording:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1RoomRecordingWithRawResponse(client, server, auth)

    async def delete_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resource to delete.
            sid: The SID of the RoomRecording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_room_recording(room_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomRecording:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the Room resource with the recording to fetch.
            sid: The SID of the RoomRecording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_recording(room_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_room_recording(
        self,
        room_sid: str,
        *,
        status: RoomRecordingEnumStatusOrStr | None = None,
        source_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomRecordingResponse:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resources to read.
            status: Read only the recordings with this status. Can be: ``processing``, ``completed``, or ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only Recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_room_recording(
                room_sid,
                status=status,
                source_sid=source_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1RoomRecordingWithRawResponse:
        return self._with_raw_response


class VideoV1RoomRecordingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resource to delete.
            sid: The SID of the RoomRecording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecording, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the Room resource with the recording to fetch.
            sid: The SID of the RoomRecording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_room_recording(
        self,
        room_sid: str,
        *,
        status: RoomRecordingEnumStatusOrStr | None = None,
        source_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomRecordingResponse, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resources to read.
            status: Read only the recordings with this status. Can be: ``processing``, ``completed``, or ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only Recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[RoomRecordingEnumStatusOrStr | None]("Status", status),
                param[str | None]("SourceSid", source_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1RoomRecordingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resource to delete.
            sid: The SID of the RoomRecording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_room_recording(
        self, room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomRecording, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the Room resource with the recording to fetch.
            sid: The SID of the RoomRecording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings/{Sid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_room_recording(
        self,
        room_sid: str,
        *,
        status: RoomRecordingEnumStatusOrStr | None = None,
        source_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomRecordingResponse, RawError]:
        """Single-track, single-media room recordings

        Args:
            room_sid: The SID of the room with the RoomRecording resources to read.
            status: Read only the recordings with this status. Can be: ``processing``, ``completed``, or ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only Recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Recordings"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[RoomRecordingEnumStatusOrStr | None]("Status", status),
                param[str | None]("SourceSid", source_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
