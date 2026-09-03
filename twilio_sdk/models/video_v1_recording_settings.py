from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class VideoV1RecordingSettings(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the RecordingSettings
    resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource and show the user in the console"""

    aws_credentials_sid: OptionalNullable[str] = UNSET
    """The SID of the stored Credential resource."""

    aws_s3_url: OptionalNullable[str] = UNSET
    """The URL of the AWS S3 bucket where the recordings are stored. We only support DNS-compliant URLs like
    ``https://documentation-example-twilio-bucket/recordings``, where ``recordings`` is the path in which you want the
    recordings to be stored. This URL accepts only URI-valid characters, as described in the `RFC 3986
    <https://tools.ietf.org/html/rfc3986#section-2>`__."""

    aws_storage_enabled: OptionalNullable[bool] = UNSET
    """Whether all recordings are written to the ``aws_s3_url``. When ``false``, all recordings are stored in our
    cloud."""

    encryption_key_sid: OptionalNullable[str] = UNSET
    """The SID of the Public Key resource used for encryption."""

    encryption_enabled: OptionalNullable[bool] = UNSET
    """Whether all recordings are stored in an encrypted form. The default is ``false``."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""


class VideoV1RecordingSettingsDict(TypedDict):
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    aws_credentials_sid: NotRequired[str | None]
    aws_s3_url: NotRequired[str | None]
    aws_storage_enabled: NotRequired[bool | None]
    encryption_key_sid: NotRequired[str | None]
    encryption_enabled: NotRequired[bool | None]
    url: NotRequired[str | None]
