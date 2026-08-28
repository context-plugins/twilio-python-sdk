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
from ..models.enums.room_transcriptions_enum_status import RoomTranscriptionsEnumStatusOrStr
from ..models.list_room_transcriptions_response import ListRoomTranscriptionsResponse
from ..models.video_v1_room_room_transcriptions import VideoV1RoomRoomTranscriptions
from ..server.server import Server


class VideoV1Transcriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1TranscriptionsWithRawResponse(client, server, auth)

    def create_room_transcriptions(
        self, room_sid: str, *, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room new transcriptions resource to be created.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_room_transcriptions(
            room_sid, configuration=configuration, request_options=request_options
        ).unwrap()

    def fetch_room_transcriptions(
        self, room_sid: str, ttid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to fetch.
            ttid: The Twilio type id of the transcriptions resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_room_transcriptions(
            room_sid, ttid, request_options=request_options
        ).unwrap()

    def list_room_transcriptions(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomTranscriptionsResponse:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_room_transcriptions(
            room_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_room_transcriptions(
        self,
        room_sid: str,
        ttid: str,
        *,
        status: RoomTranscriptionsEnumStatusOrStr | None = None,
        configuration: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to update.
            ttid: The Twilio type id of the transcriptions resource to update.
            status: The status of the transcriptions resource.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_room_transcriptions(
            room_sid, ttid, status=status, configuration=configuration, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1TranscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1Transcriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1TranscriptionsWithRawResponse(client, server, auth)

    async def create_room_transcriptions(
        self, room_sid: str, *, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room new transcriptions resource to be created.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_room_transcriptions(
                room_sid, configuration=configuration, request_options=request_options
            )
        ).unwrap()

    async def fetch_room_transcriptions(
        self, room_sid: str, ttid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to fetch.
            ttid: The Twilio type id of the transcriptions resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_room_transcriptions(room_sid, ttid, request_options=request_options)
        ).unwrap()

    async def list_room_transcriptions(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoomTranscriptionsResponse:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_room_transcriptions(
                room_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_room_transcriptions(
        self,
        room_sid: str,
        ttid: str,
        *,
        status: RoomTranscriptionsEnumStatusOrStr | None = None,
        configuration: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1RoomRoomTranscriptions:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to update.
            ttid: The Twilio type id of the transcriptions resource to update.
            status: The status of the transcriptions resource.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_room_transcriptions(
                room_sid, ttid, status=status, configuration=configuration, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1TranscriptionsWithRawResponse:
        return self._with_raw_response


class VideoV1TranscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_room_transcriptions(
        self, room_sid: str, *, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room new transcriptions resource to be created.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions"),
            path_params=[param[str]("RoomSid", room_sid)],
            body=form_body([param[Any | None]("Configuration", configuration)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_room_transcriptions(
        self, room_sid: str, ttid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to fetch.
            ttid: The Twilio type id of the transcriptions resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions/{Ttid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Ttid", ttid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_room_transcriptions(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomTranscriptionsResponse, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomTranscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_room_transcriptions(
        self,
        room_sid: str,
        ttid: str,
        *,
        status: RoomTranscriptionsEnumStatusOrStr | None = None,
        configuration: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to update.
            ttid: The Twilio type id of the transcriptions resource to update.
            status: The status of the transcriptions resource.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions/{Ttid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Ttid", ttid)],
            body=form_body(
                [
                    param[RoomTranscriptionsEnumStatusOrStr | None]("Status", status),
                    param[Any | None]("Configuration", configuration),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1TranscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_room_transcriptions(
        self, room_sid: str, *, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room new transcriptions resource to be created.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions"),
            path_params=[param[str]("RoomSid", room_sid)],
            body=form_body([param[Any | None]("Configuration", configuration)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_room_transcriptions(
        self, room_sid: str, ttid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to fetch.
            ttid: The Twilio type id of the transcriptions resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions/{Ttid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Ttid", ttid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_room_transcriptions(
        self,
        room_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoomTranscriptionsResponse, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions"),
            path_params=[param[str]("RoomSid", room_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoomTranscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_room_transcriptions(
        self,
        room_sid: str,
        ttid: str,
        *,
        status: RoomTranscriptionsEnumStatusOrStr | None = None,
        configuration: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1RoomRoomTranscriptions, RawError]:
        """transcriptions in video rooms

        Args:
            room_sid: The SID of the room with the transcriptions resource to update.
            ttid: The Twilio type id of the transcriptions resource to update.
            status: The status of the transcriptions resource.
            configuration: A collection of properties that describe transcription behaviour.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Rooms/{RoomSid}/Transcriptions/{Ttid}"),
            path_params=[param[str]("RoomSid", room_sid), param[str]("Ttid", ttid)],
            body=form_body(
                [
                    param[RoomTranscriptionsEnumStatusOrStr | None]("Status", status),
                    param[Any | None]("Configuration", configuration),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1RoomRoomTranscriptions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
