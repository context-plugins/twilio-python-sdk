from __future__ import annotations

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
from ..models.video_v1_composition_settings import VideoV1CompositionSettings
from ..server.server import Server


class VideoV1CompositionSettingsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideoV1CompositionSettingsApiWithRawResponse(client, server, auth)

    def create_composition_settings(
        self,
        friendly_name: str,
        *,
        aws_credentials_sid: str | None = None,
        encryption_key_sid: str | None = None,
        aws_s3_url: str | None = None,
        aws_storage_enabled: bool | None = None,
        encryption_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionSettings:
        """Recording composition settings

        Args:
            friendly_name: A descriptive string that you create to describe the resource and show to the user in the
                console
            aws_credentials_sid: The SID of the stored Credential resource.
            encryption_key_sid: The SID of the Public Key resource to use for encryption.
            aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support
                DNS-compliant URLs like ``https://documentation-example-twilio-bucket/compositions``, where
                ``compositions`` is the path in which you want the compositions to be stored. This URL accepts only
                URI-valid characters, as described in the `RFC 3986 <https://tools.ietf.org/html/rfc3986#section-2>`__.
            aws_storage_enabled: Whether all compositions should be written to the ``aws_s3_url``. When ``false``, all
                compositions are stored in our cloud.
            encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_composition_settings(
            friendly_name,
            aws_credentials_sid=aws_credentials_sid,
            encryption_key_sid=encryption_key_sid,
            aws_s3_url=aws_s3_url,
            aws_storage_enabled=aws_storage_enabled,
            encryption_enabled=encryption_enabled,
            request_options=request_options,
        ).unwrap()

    def fetch_composition_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1CompositionSettings:
        """Recording composition settings

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_composition_settings(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideoV1CompositionSettingsApiWithRawResponse:
        return self._with_raw_response


class AsyncVideoV1CompositionSettingsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideoV1CompositionSettingsApiWithRawResponse(client, server, auth)

    async def create_composition_settings(
        self,
        friendly_name: str,
        *,
        aws_credentials_sid: str | None = None,
        encryption_key_sid: str | None = None,
        aws_s3_url: str | None = None,
        aws_storage_enabled: bool | None = None,
        encryption_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoV1CompositionSettings:
        """Recording composition settings

        Args:
            friendly_name: A descriptive string that you create to describe the resource and show to the user in the
                console
            aws_credentials_sid: The SID of the stored Credential resource.
            encryption_key_sid: The SID of the Public Key resource to use for encryption.
            aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support
                DNS-compliant URLs like ``https://documentation-example-twilio-bucket/compositions``, where
                ``compositions`` is the path in which you want the compositions to be stored. This URL accepts only
                URI-valid characters, as described in the `RFC 3986 <https://tools.ietf.org/html/rfc3986#section-2>`__.
            aws_storage_enabled: Whether all compositions should be written to the ``aws_s3_url``. When ``false``, all
                compositions are stored in our cloud.
            encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_composition_settings(
                friendly_name,
                aws_credentials_sid=aws_credentials_sid,
                encryption_key_sid=encryption_key_sid,
                aws_s3_url=aws_s3_url,
                aws_storage_enabled=aws_storage_enabled,
                encryption_enabled=encryption_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_composition_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoV1CompositionSettings:
        """Recording composition settings

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_composition_settings(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideoV1CompositionSettingsApiWithRawResponse:
        return self._with_raw_response


class VideoV1CompositionSettingsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_composition_settings(
        self,
        friendly_name: str,
        *,
        aws_credentials_sid: str | None = None,
        encryption_key_sid: str | None = None,
        aws_s3_url: str | None = None,
        aws_storage_enabled: bool | None = None,
        encryption_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionSettings, RawError]:
        """Recording composition settings

        Args:
            friendly_name: A descriptive string that you create to describe the resource and show to the user in the
                console
            aws_credentials_sid: The SID of the stored Credential resource.
            encryption_key_sid: The SID of the Public Key resource to use for encryption.
            aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support
                DNS-compliant URLs like ``https://documentation-example-twilio-bucket/compositions``, where
                ``compositions`` is the path in which you want the compositions to be stored. This URL accepts only
                URI-valid characters, as described in the `RFC 3986 <https://tools.ietf.org/html/rfc3986#section-2>`__.
            aws_storage_enabled: Whether all compositions should be written to the ``aws_s3_url``. When ``false``, all
                compositions are stored in our cloud.
            encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionSettings/Default"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("AwsCredentialsSid", aws_credentials_sid),
                    param[str | None]("EncryptionKeySid", encryption_key_sid),
                    param[str | None]("AwsS3Url", aws_s3_url),
                    param[bool | None]("AwsStorageEnabled", aws_storage_enabled),
                    param[bool | None]("EncryptionEnabled", encryption_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_composition_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1CompositionSettings, RawError]:
        """Recording composition settings

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionSettings/Default"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideoV1CompositionSettingsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_composition_settings(
        self,
        friendly_name: str,
        *,
        aws_credentials_sid: str | None = None,
        encryption_key_sid: str | None = None,
        aws_s3_url: str | None = None,
        aws_storage_enabled: bool | None = None,
        encryption_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoV1CompositionSettings, RawError]:
        """Recording composition settings

        Args:
            friendly_name: A descriptive string that you create to describe the resource and show to the user in the
                console
            aws_credentials_sid: The SID of the stored Credential resource.
            encryption_key_sid: The SID of the Public Key resource to use for encryption.
            aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support
                DNS-compliant URLs like ``https://documentation-example-twilio-bucket/compositions``, where
                ``compositions`` is the path in which you want the compositions to be stored. This URL accepts only
                URI-valid characters, as described in the `RFC 3986 <https://tools.ietf.org/html/rfc3986#section-2>`__.
            aws_storage_enabled: Whether all compositions should be written to the ``aws_s3_url``. When ``false``, all
                compositions are stored in our cloud.
            encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/v1/CompositionSettings/Default"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("AwsCredentialsSid", aws_credentials_sid),
                    param[str | None]("EncryptionKeySid", encryption_key_sid),
                    param[str | None]("AwsS3Url", aws_s3_url),
                    param[bool | None]("AwsStorageEnabled", aws_storage_enabled),
                    param[bool | None]("EncryptionEnabled", encryption_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_composition_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoV1CompositionSettings, RawError]:
        """Recording composition settings

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default6("/v1/CompositionSettings/Default"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VideoV1CompositionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
