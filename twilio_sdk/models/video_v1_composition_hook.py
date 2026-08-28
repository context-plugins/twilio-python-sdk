from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.composition_hook_enum_format import CompositionHookEnumFormatOrStr


class VideoV1CompositionHook(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the CompositionHook
    resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource. Can be up to 100 characters long and must be unique within
    the account."""

    enabled: OptionalNullable[bool] = UNSET
    """Whether the CompositionHook is active. When ``true``, the CompositionHook is triggered for every completed Group
    Room on the account. When ``false``, the CompositionHook is never triggered."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the CompositionHook resource."""

    audio_sources: Optional[list[str | None]] = UNSET
    """The array of track names to include in the compositions created by the composition hook. A composition triggered
    by the composition hook includes all audio sources specified in ``audio_sources`` except those specified in
    ``audio_sources_excluded``. The track names in this property can include an asterisk as a wild card character, which
    matches zero or more characters in a track name. For example, ``student*`` includes tracks named ``student`` as well
    as ``studentTeam``. Please, be aware that either video_layout or audio_sources have to be provided to get a valid
    creation request"""

    audio_sources_excluded: Optional[list[str | None]] = UNSET
    """The array of track names to exclude from the compositions created by the composition hook. A composition
    triggered by the composition hook includes all audio sources specified in ``audio_sources`` except for those
    specified in ``audio_sources_excluded``. The track names in this property can include an asterisk as a wild card
    character, which matches zero or more characters in a track name. For example, ``student*`` excludes ``student`` as
    well as ``studentTeam``. This parameter can also be empty."""

    video_layout: OptionalNullable[Any] = UNSET
    """A JSON object that describes the video layout of the composition in terms of regions as specified in the HTTP
    POST request that created the CompositionHook resource. See `POST Parameters
    <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more information. Please,
    be aware that either video_layout or audio_sources have to be provided to get a valid creation request"""

    resolution: OptionalNullable[str] = UNSET
    """The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string's format
    is ``{width}x{height}``, such as ``640x480``."""

    trim: OptionalNullable[bool] = UNSET
    """Whether intervals with no media are clipped, as specified in the POST request that created the CompositionHook
    resource. Compositions with ``trim`` enabled are shorter when the Room is created and no Participant joins for a
    while as well as if all the Participants leave the room and join later, because those gaps will be removed. See
    `Specifying Video Layouts <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__
    for more info."""

    format: Optional[CompositionHookEnumFormatOrStr] = UNSET
    """The container format of the media files used by the compositions created by the composition hook. If ``mp4`` or
    ``webm``, ``audio_sources`` must have one or more tracks and/or a ``video_layout`` element must contain a valid
    ``video_sources`` list, otherwise an error occurs."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using the ``status_callback_method`` to send status information to your application."""

    status_callback_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method we should use to call ``status_callback``. Can be ``POST`` or ``GET`` and defaults to
    ``POST``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class VideoV1CompositionHookDict(TypedDict):
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    enabled: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    audio_sources: NotRequired[list[str | None]]
    audio_sources_excluded: NotRequired[list[str | None]]
    video_layout: NotRequired[Any | None]
    resolution: NotRequired[str | None]
    trim: NotRequired[bool | None]
    format: NotRequired[CompositionHookEnumFormatOrStr]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    url: NotRequired[AnyUrl | None]
