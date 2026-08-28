from __future__ import annotations

from typing import Any

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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.composition_enum_format import CompositionEnumFormatOrStr
from ..models.enums.composition_enum_status import CompositionEnumStatusOrStr
from ..models.list_composition_response import ListCompositionResponse
from ..models.video_v1_composition import VideoV1Composition
from ..server.server import Server


class VideoV1CompositionApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1CompositionApiWithRawResponse(client, server, auth)

    def create_composition(
        self,
        room_sid: str,
        *,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionEnumFormatOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Composition:
        """Recording compositions

        Args:
            room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
            video_layout: An object that describes the video layout of the composition in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
                Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation
                request
            audio_sources: An array of track names from the same group room to merge into the new composition. Can
                include zero or more track names. The new composition includes all audio sources specified in
                ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names in this
                parameter can include an asterisk as a wild card character, which will match zero or more characters in
                a track name. For example, ``student*`` includes ``student`` as well as ``studentTeam``. Please, be
                aware that either video_layout or audio_sources have to be provided to get a valid creation request
            audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources
                specified in ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names
                in this parameter can include an asterisk as a wild card character, which will match zero or more
                characters in a track name. For example, ``student*`` excludes ``student`` as well as ``studentTeam``.
                This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the composition's media files as specified in the POST request that created
                the Composition resource. See `POST Parameters
                <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more
                information.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the composition. The default is
                ``true``. Compositions with ``trim`` enabled are shorter when the Room is created and no Participant
                joins for a while as well as if all the Participants leave the room and join later, because those gaps
                will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_composition(
            room_sid,
            video_layout=video_layout,
            audio_sources=audio_sources,
            audio_sources_excluded=audio_sources_excluded,
            resolution=resolution,
            format=format,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            trim=trim,
            request_options=request_options,
        ).unwrap()

    def delete_composition(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_composition(sid, request_options=request_options).unwrap()

    def fetch_composition(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VideoV1Composition:
        """Returns a single Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_composition(sid, request_options=request_options).unwrap()

    def list_composition(
        self,
        *,
        status: CompositionEnumStatusOrStr | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        room_sid: str | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompositionResponse:
        """List of all Recording compositions.

        Args:
            status: Read only Composition resources with this status. Can be: ``enqueued``, ``processing``,
                ``completed``, ``deleted``, or ``failed``.
            date_created_after: Read only Composition resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
            room_sid: Read only Composition resources with this Room SID.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_composition(
            status=status,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1CompositionApiWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1CompositionApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1CompositionApiWithRawResponse(client, server, auth)

    async def create_composition(
        self,
        room_sid: str,
        *,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionEnumFormatOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1Composition:
        """Recording compositions

        Args:
            room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
            video_layout: An object that describes the video layout of the composition in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
                Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation
                request
            audio_sources: An array of track names from the same group room to merge into the new composition. Can
                include zero or more track names. The new composition includes all audio sources specified in
                ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names in this
                parameter can include an asterisk as a wild card character, which will match zero or more characters in
                a track name. For example, ``student*`` includes ``student`` as well as ``studentTeam``. Please, be
                aware that either video_layout or audio_sources have to be provided to get a valid creation request
            audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources
                specified in ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names
                in this parameter can include an asterisk as a wild card character, which will match zero or more
                characters in a track name. For example, ``student*`` excludes ``student`` as well as ``studentTeam``.
                This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the composition's media files as specified in the POST request that created
                the Composition resource. See `POST Parameters
                <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more
                information.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the composition. The default is
                ``true``. Compositions with ``trim`` enabled are shorter when the Room is created and no Participant
                joins for a while as well as if all the Participants leave the room and join later, because those gaps
                will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_composition(
                room_sid,
                video_layout=video_layout,
                audio_sources=audio_sources,
                audio_sources_excluded=audio_sources_excluded,
                resolution=resolution,
                format=format,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                trim=trim,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_composition(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_composition(sid, request_options=request_options)).unwrap()

    async def fetch_composition(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1Composition:
        """Returns a single Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_composition(sid, request_options=request_options)).unwrap()

    async def list_composition(
        self,
        *,
        status: CompositionEnumStatusOrStr | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        room_sid: str | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompositionResponse:
        """List of all Recording compositions.

        Args:
            status: Read only Composition resources with this status. Can be: ``enqueued``, ``processing``,
                ``completed``, ``deleted``, or ``failed``.
            date_created_after: Read only Composition resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
            room_sid: Read only Composition resources with this Room SID.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_composition(
                status=status,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                room_sid=room_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1CompositionApiWithRawResponse:
        return self._with_raw_response


class VideoV1CompositionApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_composition(
        self,
        room_sid: str,
        *,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionEnumFormatOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Composition, RawError]:
        """Recording compositions

        Args:
            room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
            video_layout: An object that describes the video layout of the composition in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
                Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation
                request
            audio_sources: An array of track names from the same group room to merge into the new composition. Can
                include zero or more track names. The new composition includes all audio sources specified in
                ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names in this
                parameter can include an asterisk as a wild card character, which will match zero or more characters in
                a track name. For example, ``student*`` includes ``student`` as well as ``studentTeam``. Please, be
                aware that either video_layout or audio_sources have to be provided to get a valid creation request
            audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources
                specified in ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names
                in this parameter can include an asterisk as a wild card character, which will match zero or more
                characters in a track name. For example, ``student*`` excludes ``student`` as well as ``studentTeam``.
                This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the composition's media files as specified in the POST request that created
                the Composition resource. See `POST Parameters
                <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more
                information.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the composition. The default is
                ``true``. Compositions with ``trim`` enabled are shorter when the Room is created and no Participant
                joins for a while as well as if all the Participants leave the room and join later, because those gaps
                will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Compositions"),
            body=form_body(
                [
                    param[str]("RoomSid", room_sid),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[str | None]("Resolution", resolution),
                    param[CompositionEnumFormatOrStr | None]("Format", format),
                    param[str | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("Trim", trim),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Composition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_composition(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Compositions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_composition(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Composition, RawError]:
        """Returns a single Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Compositions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Composition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_composition(
        self,
        *,
        status: CompositionEnumStatusOrStr | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        room_sid: str | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompositionResponse, RawError]:
        """List of all Recording compositions.

        Args:
            status: Read only Composition resources with this status. Can be: ``enqueued``, ``processing``,
                ``completed``, ``deleted``, or ``failed``.
            date_created_after: Read only Composition resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
            room_sid: Read only Composition resources with this Room SID.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Compositions"),
            query_params=[
                param[CompositionEnumStatusOrStr | None]("Status", status),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("RoomSid", room_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCompositionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1CompositionApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_composition(
        self,
        room_sid: str,
        *,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionEnumFormatOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1Composition, RawError]:
        """Recording compositions

        Args:
            room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
            video_layout: An object that describes the video layout of the composition in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
                Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation
                request
            audio_sources: An array of track names from the same group room to merge into the new composition. Can
                include zero or more track names. The new composition includes all audio sources specified in
                ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names in this
                parameter can include an asterisk as a wild card character, which will match zero or more characters in
                a track name. For example, ``student*`` includes ``student`` as well as ``studentTeam``. Please, be
                aware that either video_layout or audio_sources have to be provided to get a valid creation request
            audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources
                specified in ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names
                in this parameter can include an asterisk as a wild card character, which will match zero or more
                characters in a track name. For example, ``student*`` excludes ``student`` as well as ``studentTeam``.
                This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the composition's media files as specified in the POST request that created
                the Composition resource. See `POST Parameters
                <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more
                information.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the composition. The default is
                ``true``. Compositions with ``trim`` enabled are shorter when the Room is created and no Participant
                joins for a while as well as if all the Participants leave the room and join later, because those gaps
                will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/Compositions"),
            body=form_body(
                [
                    param[str]("RoomSid", room_sid),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[str | None]("Resolution", resolution),
                    param[CompositionEnumFormatOrStr | None]("Format", format),
                    param[str | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("Trim", trim),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Composition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_composition(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/Compositions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_composition(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1Composition, RawError]:
        """Returns a single Composition resource identified by a Composition SID.

        Args:
            sid: The SID of the Composition resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Compositions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1Composition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_composition(
        self,
        *,
        status: CompositionEnumStatusOrStr | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        room_sid: str | None = None,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompositionResponse, RawError]:
        """List of all Recording compositions.

        Args:
            status: Read only Composition resources with this status. Can be: ``enqueued``, ``processing``,
                ``completed``, ``deleted``, or ``failed``.
            date_created_after: Read only Composition resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time with time zone.
            date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
            room_sid: Read only Composition resources with this Room SID.
            page_size: How many resources to return in each list page.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/Compositions"),
            query_params=[
                param[CompositionEnumStatusOrStr | None]("Status", status),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("RoomSid", room_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCompositionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
