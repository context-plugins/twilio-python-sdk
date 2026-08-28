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
from ..models.enums.recording_enum_status1 import RecordingEnumStatus1OrStr
from ..models.enums.recording_enum_type import RecordingEnumTypeOrStr
from ..models.list_recording_response1 import ListRecordingResponse1
from ..models.video_v1_recording import VideoV1Recording
from ..server.server import Server


class VideoV1RecordingApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1RecordingApiWithRawResponse(client, server, auth)

    def delete_recording2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_recording2(sid, request_options=request_options).unwrap()

    def fetch_recording2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VideoV1Recording:
        """Returns a single Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_recording2(sid, request_options=request_options).unwrap()

    def list_recording2(
        self,
        *,
        status: RecordingEnumStatus1OrStr | None = None,
        source_sid: str | None = None,
        grouping_sid: list[str] | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        media_type: RecordingEnumTypeOrStr | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingResponse1:
        """List of all Track recordings.

        Args:
            status: Read only the recordings that have this status. Can be: ``processing``, ``completed``, or
                ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            grouping_sid: Read only recordings with this ``grouping_sid``, which may include a ``participant_sid``
                and/or a ``room_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone, given as
                ``YYYY-MM-DDThh:mm:ss+|-hh:mm`` or ``YYYY-MM-DDThh:mm:ssZ``.
            media_type: Read only recordings that have this media type. Can be either ``audio`` or ``video``.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_recording2(
            status=status,
            source_sid=source_sid,
            grouping_sid=grouping_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            media_type=media_type,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1RecordingApiWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1RecordingApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1RecordingApiWithRawResponse(client, server, auth)

    async def delete_recording2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_recording2(sid, request_options=request_options)).unwrap()

    async def fetch_recording2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1Recording:
        """Returns a single Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_recording2(sid, request_options=request_options)).unwrap()

    async def list_recording2(
        self,
        *,
        status: RecordingEnumStatus1OrStr | None = None,
        source_sid: str | None = None,
        grouping_sid: list[str] | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        media_type: RecordingEnumTypeOrStr | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingResponse1:
        """List of all Track recordings.

        Args:
            status: Read only the recordings that have this status. Can be: ``processing``, ``completed``, or
                ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            grouping_sid: Read only recordings with this ``grouping_sid``, which may include a ``participant_sid``
                and/or a ``room_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone, given as
                ``YYYY-MM-DDThh:mm:ss+|-hh:mm`` or ``YYYY-MM-DDThh:mm:ssZ``.
            media_type: Read only recordings that have this media type. Can be either ``audio`` or ``video``.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_recording2(
                status=status,
                source_sid=source_sid,
                grouping_sid=grouping_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                media_type=media_type,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1RecordingApiWithRawResponse:
        return self._with_raw_response


class VideoV1RecordingApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_recording2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Recordings/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_recording2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Recording, RawError]:
        """Returns a single Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Recordings/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Recording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_recording2(
        self,
        *,
        status: RecordingEnumStatus1OrStr | None = None,
        source_sid: str | None = None,
        grouping_sid: list[str] | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        media_type: RecordingEnumTypeOrStr | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingResponse1, RawError]:
        """List of all Track recordings.

        Args:
            status: Read only the recordings that have this status. Can be: ``processing``, ``completed``, or
                ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            grouping_sid: Read only recordings with this ``grouping_sid``, which may include a ``participant_sid``
                and/or a ``room_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone, given as
                ``YYYY-MM-DDThh:mm:ss+|-hh:mm`` or ``YYYY-MM-DDThh:mm:ssZ``.
            media_type: Read only recordings that have this media type. Can be either ``audio`` or ``video``.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Recordings"),
            query_params=[
                param[RecordingEnumStatus1OrStr | None]("Status", status),
                param[str | None]("SourceSid", source_sid),
                param[list[str] | None]("GroupingSid", grouping_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[RecordingEnumTypeOrStr | None]("MediaType", media_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1RecordingApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_recording2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Recordings/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_recording2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Recording, RawError]:
        """Returns a single Recording resource identified by a Recording SID.

        Args:
            sid: The SID of the Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Recordings/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Recording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_recording2(
        self,
        *,
        status: RecordingEnumStatus1OrStr | None = None,
        source_sid: str | None = None,
        grouping_sid: list[str] | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        media_type: RecordingEnumTypeOrStr | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingResponse1, RawError]:
        """List of all Track recordings.

        Args:
            status: Read only the recordings that have this status. Can be: ``processing``, ``completed``, or
                ``deleted``.
            source_sid: Read only the recordings that have this ``source_sid``.
            grouping_sid: Read only recordings with this ``grouping_sid``, which may include a ``participant_sid``
                and/or a ``room_sid``.
            date_created_after: Read only recordings that started on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only recordings that started before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone, given as
                ``YYYY-MM-DDThh:mm:ss+|-hh:mm`` or ``YYYY-MM-DDThh:mm:ssZ``.
            media_type: Read only recordings that have this media type. Can be either ``audio`` or ``video``.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Recordings"),
            query_params=[
                param[RecordingEnumStatus1OrStr | None]("Status", status),
                param[str | None]("SourceSid", source_sid),
                param[list[str] | None]("GroupingSid", grouping_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[RecordingEnumTypeOrStr | None]("MediaType", media_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
