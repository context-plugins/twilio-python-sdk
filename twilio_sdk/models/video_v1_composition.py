from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.composition_enum_format import CompositionEnumFormatOrStr
from .enums.composition_enum_status import CompositionEnumStatusOrStr


class VideoV1Composition(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Composition
    resource."""

    status: Optional[CompositionEnumStatusOrStr] = UNSET
    """The status of the composition. Can be: ``enqueued``, ``processing``, ``completed``, ``deleted`` or ``failed``.
    ``enqueued`` is the initial state and indicates that the composition request has been received and is scheduled for
    processing; ``processing`` indicates the composition is being processed; ``completed`` indicates the composition has
    been completed and is available for download; ``deleted`` means the composition media has been deleted from the
    system, but its metadata is still available for 30 days; ``failed`` indicates the composition failed to execute the
    media processing task."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_completed: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the composition's media processing task finished, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_deleted: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the composition generated media was deleted, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Composition resource."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the Group Room that generated the audio and video tracks used in the composition. All media sources
    included in a composition must belong to the same Group Room."""

    audio_sources: Optional[list[str | None]] = UNSET
    """The array of track names to include in the composition. The composition includes all audio sources specified in
    ``audio_sources`` except those specified in ``audio_sources_excluded``. The track names in this property can include
    an asterisk as a wild card character, which matches zero or more characters in a track name. For example,
    ``student*`` includes tracks named ``student`` as well as ``studentTeam``."""

    audio_sources_excluded: Optional[list[str | None]] = UNSET
    """The array of track names to exclude from the composition. The composition includes all audio sources specified in
    ``audio_sources`` except for those specified in ``audio_sources_excluded``. The track names in this property can
    include an asterisk as a wild card character, which matches zero or more characters in a track name. For example,
    ``student*`` excludes ``student`` as well as ``studentTeam``. This parameter can also be empty."""

    video_layout: OptionalNullable[Any] = UNSET
    """An object that describes the video layout of the composition in terms of regions. See `Specifying Video Layouts
    <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info."""

    resolution: OptionalNullable[str] = UNSET
    """The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string's format
    is ``{width}x{height}``, such as ``640x480``."""

    trim: OptionalNullable[bool] = UNSET
    """Whether to remove intervals with no media, as specified in the POST request that created the composition.
    Compositions with ``trim`` enabled are shorter when the Room is created and no Participant joins for a while as well
    as if all the Participants leave the room and join later, because those gaps will be removed. See `Specifying Video
    Layouts <https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts>`__ for more info."""

    format: Optional[CompositionEnumFormatOrStr] = UNSET
    """The container format of the composition's media files as specified in the POST request that created the
    Composition resource. See `POST Parameters
    <https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters>`__ for more information."""

    bitrate: Optional[int] = UNSET
    """The average bit rate of the composition's media."""

    size: OptionalNullable[int] = UNSET
    """The size of the composed media file in bytes."""

    duration: Optional[int] = UNSET
    """The duration of the composition's media file in seconds."""

    media_external_location: OptionalNullable[AnyUrl] = UNSET
    """The URL of the media file associated with the composition when stored externally. See `External S3 Compositions
    </docs/video/api/external-s3-compositions>`__ for more details."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL called using the ``status_callback_method`` to send status information on every composition event."""

    status_callback_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method used to call ``status_callback``. Can be: ``POST`` or ``GET``, defaults to ``POST``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URL of the media file associated with the composition."""


class VideoV1CompositionDict(TypedDict):
    account_sid: NotRequired[str | None]
    status: NotRequired[CompositionEnumStatusOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_completed: NotRequired[RFC3339DateTime | None]
    date_deleted: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    audio_sources: NotRequired[list[str | None]]
    audio_sources_excluded: NotRequired[list[str | None]]
    video_layout: NotRequired[Any | None]
    resolution: NotRequired[str | None]
    trim: NotRequired[bool | None]
    format: NotRequired[CompositionEnumFormatOrStr]
    bitrate: NotRequired[int]
    size: NotRequired[int | None]
    duration: NotRequired[int]
    media_external_location: NotRequired[AnyUrl | None]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
