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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.composition_hook_enum_format import CompositionHookEnumFormatOrStr
from ..models.list_composition_hook_response import ListCompositionHookResponse
from ..models.video_v1_composition_hook import VideoV1CompositionHook
from ..server.server import Server


class VideoV1CompositionHookApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1CompositionHookApiWithRawResponse(client, server, auth)

    def create_composition_hook(
        self,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionHook:
        """Recording composition hooks

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook will never be triggered.
            video_layout: An object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_composition_hook(
            friendly_name,
            enabled=enabled,
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

    def delete_composition_hook(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording CompositionHook resource identified by a ``CompositionHook SID``.

        Args:
            sid: The SID of the CompositionHook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_composition_hook(sid, request_options=request_options).unwrap()

    def fetch_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1CompositionHook:
        """Returns a single CompositionHook resource identified by a CompositionHook SID.

        Args:
            sid: The SID of the CompositionHook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_composition_hook(sid, request_options=request_options).unwrap()

    def list_composition_hook(
        self,
        *,
        enabled: bool | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompositionHookResponse:
        """List of all Recording CompositionHook resources.

        Args:
            enabled: Read only CompositionHook resources with an ``enabled`` value that matches this parameter.
            date_created_after: Read only CompositionHook resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only CompositionHook resources created before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is
                not case sensitive and can include asterisk ``*`` characters as wildcard match.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_composition_hook(
            enabled=enabled,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_composition_hook(
        self,
        sid: str,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        trim: bool | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        resolution: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionHook:
        """Recording composition hooks

        Args:
            sid: The SID of the CompositionHook resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook never triggers.
            video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            trim: Whether to clip the intervals where there is no active media in the compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_composition_hook(
            sid,
            friendly_name,
            enabled=enabled,
            video_layout=video_layout,
            audio_sources=audio_sources,
            audio_sources_excluded=audio_sources_excluded,
            trim=trim,
            format=format,
            resolution=resolution,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideoV1CompositionHookApiWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1CompositionHookApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1CompositionHookApiWithRawResponse(client, server, auth)

    async def create_composition_hook(
        self,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionHook:
        """Recording composition hooks

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook will never be triggered.
            video_layout: An object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_composition_hook(
                friendly_name,
                enabled=enabled,
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

    async def delete_composition_hook(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Recording CompositionHook resource identified by a ``CompositionHook SID``.

        Args:
            sid: The SID of the CompositionHook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_composition_hook(sid, request_options=request_options)).unwrap()

    async def fetch_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1CompositionHook:
        """Returns a single CompositionHook resource identified by a CompositionHook SID.

        Args:
            sid: The SID of the CompositionHook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_composition_hook(sid, request_options=request_options)).unwrap()

    async def list_composition_hook(
        self,
        *,
        enabled: bool | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompositionHookResponse:
        """List of all Recording CompositionHook resources.

        Args:
            enabled: Read only CompositionHook resources with an ``enabled`` value that matches this parameter.
            date_created_after: Read only CompositionHook resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only CompositionHook resources created before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is
                not case sensitive and can include asterisk ``*`` characters as wildcard match.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_composition_hook(
                enabled=enabled,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_composition_hook(
        self,
        sid: str,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        trim: bool | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        resolution: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionHook:
        """Recording composition hooks

        Args:
            sid: The SID of the CompositionHook resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook never triggers.
            video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            trim: Whether to clip the intervals where there is no active media in the compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_composition_hook(
                sid,
                friendly_name,
                enabled=enabled,
                video_layout=video_layout,
                audio_sources=audio_sources,
                audio_sources_excluded=audio_sources_excluded,
                trim=trim,
                format=format,
                resolution=resolution,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1CompositionHookApiWithRawResponse:
        return self._with_raw_response


class VideoV1CompositionHookApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_composition_hook(
        self,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Recording composition hooks

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook will never be triggered.
            video_layout: An object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionHooks"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[bool | None]("Enabled", enabled),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[str | None]("Resolution", resolution),
                    param[CompositionHookEnumFormatOrStr | None]("Format", format),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("Trim", trim),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording CompositionHook resource identified by a ``CompositionHook SID``.

        Args:
            sid: The SID of the CompositionHook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Returns a single CompositionHook resource identified by a CompositionHook SID.

        Args:
            sid: The SID of the CompositionHook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_composition_hook(
        self,
        *,
        enabled: bool | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompositionHookResponse, RawError]:
        """List of all Recording CompositionHook resources.

        Args:
            enabled: Read only CompositionHook resources with an ``enabled`` value that matches this parameter.
            date_created_after: Read only CompositionHook resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only CompositionHook resources created before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is
                not case sensitive and can include asterisk ``*`` characters as wildcard match.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionHooks"),
            query_params=[
                param[bool | None]("Enabled", enabled),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCompositionHookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_composition_hook(
        self,
        sid: str,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        trim: bool | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        resolution: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Recording composition hooks

        Args:
            sid: The SID of the CompositionHook resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook never triggers.
            video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            trim: Whether to clip the intervals where there is no active media in the compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[bool | None]("Enabled", enabled),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[bool | None]("Trim", trim),
                    param[CompositionHookEnumFormatOrStr | None]("Format", format),
                    param[str | None]("Resolution", resolution),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1CompositionHookApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_composition_hook(
        self,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        resolution: str | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Recording composition hooks

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook will never be triggered.
            video_layout: An object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionHooks"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[bool | None]("Enabled", enabled),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[str | None]("Resolution", resolution),
                    param[CompositionHookEnumFormatOrStr | None]("Format", format),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("Trim", trim),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Recording CompositionHook resource identified by a ``CompositionHook SID``.

        Args:
            sid: The SID of the CompositionHook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_composition_hook(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Returns a single CompositionHook resource identified by a CompositionHook SID.

        Args:
            sid: The SID of the CompositionHook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_composition_hook(
        self,
        *,
        enabled: bool | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompositionHookResponse, RawError]:
        """List of all Recording CompositionHook resources.

        Args:
            enabled: Read only CompositionHook resources with an ``enabled`` value that matches this parameter.
            date_created_after: Read only CompositionHook resources created on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            date_created_before: Read only CompositionHook resources created before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ datetime with time zone.
            friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is
                not case sensitive and can include asterisk ``*`` characters as wildcard match.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionHooks"),
            query_params=[
                param[bool | None]("Enabled", enabled),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCompositionHookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_composition_hook(
        self,
        sid: str,
        friendly_name: str,
        *,
        enabled: bool | None = None,
        video_layout: Any | None = None,
        audio_sources: list[str] | None = None,
        audio_sources_excluded: list[str] | None = None,
        trim: bool | None = None,
        format: CompositionHookEnumFormatOrStr | None = None,
        resolution: str | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionHook, RawError]:
        """Recording composition hooks

        Args:
            sid: The SID of the CompositionHook resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 100 characters
                long and it must be unique within the account.
            enabled: Whether the composition hook is active. When ``true``, the composition hook will be triggered for
                every completed Group Room in the account. When ``false``, the composition hook never triggers.
            video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See
                `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            audio_sources: An array of track names from the same group room to merge into the compositions created by
                the composition hook. Can include zero or more track names. A composition triggered by the composition
                hook includes all audio sources specified in ``audio_sources`` except those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` includes
                tracks named ``student`` as well as ``studentTeam``.
            audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook
                includes all audio sources specified in ``audio_sources`` except for those specified in
                ``audio_sources_excluded``. The track names in this parameter can include an asterisk as a wild card
                character, which matches zero or more characters in a track name. For example, ``student*`` excludes
                ``student`` as well as ``studentTeam``. This parameter can also be empty.
            trim: Whether to clip the intervals where there is no active media in the compositions triggered by the
                composition hook. The default is ``true``. Compositions with ``trim`` enabled are shorter when the Room
                is created and no Participant joins for a while as well as if all the Participants leave the room and
                join later, because those gaps will be removed. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            format: The container format of the media files used by the compositions created by the composition hook. If
                ``mp4`` or ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element
                must contain a valid ``video_sources`` list, otherwise an error occurs.
            resolution: A string that describes the columns (width) and rows (height) of the generated composed video in
                pixels. Defaults to ``640x480``. The string's format is ``{width}x{height}`` where: * 16 <= ``{width}``
                <= 1280 * 16 <= ``{height}`` <= 1280 * ``{width}`` * ``{height}`` <= 921,600 Typical values are: * HD =
                ``1280x720`` * PAL = ``1024x576`` * VGA = ``640x480`` * CIF = ``320x240`` Note that the ``resolution``
                imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by
                the aspect ratio, they are scaled to fit. See `Specifying Video Layouts
                <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application on every composition event. If not provided, status callback events will not be
                dispatched.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionHooks/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[bool | None]("Enabled", enabled),
                    param[Any | None]("VideoLayout", video_layout),
                    param[list[str] | None]("AudioSources", audio_sources),
                    param[list[str] | None]("AudioSourcesExcluded", audio_sources_excluded),
                    param[bool | None]("Trim", trim),
                    param[CompositionHookEnumFormatOrStr | None]("Format", format),
                    param[str | None]("Resolution", resolution),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionHook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
