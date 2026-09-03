from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountMessageMedia(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with this Media resource."""

    content_type: OptionalNullable[str] = UNSET
    """The default `MIME type <https://en.wikipedia.org/wiki/Internet_media_type>`__ of the media, for example
    ``image/jpeg``, ``image/png``, or ``image/gif``."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT when this Media resource was created, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT when this Media resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    parent_sid: OptionalNullable[str] = UNSET
    """The SID of the Message resource that is associated with this Media resource."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies this Media resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI of this Media resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountMessageMediaDict(TypedDict):
    account_sid: NotRequired[str | None]
    content_type: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    parent_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    uri: NotRequired[str | None]
