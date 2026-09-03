from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.messaging_v1_brand_registrations_brand_registration_otp import (
    MessagingV1BrandRegistrationsBrandRegistrationOtp,
)
from ..server.server import Server


class MessagingV1BrandRegistrationOtp:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1BrandRegistrationOtpWithRawResponse(client, server, auth)

    def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrationsBrandRegistrationOtp:
        """A Messaging Service resource to retry OTP verification for Sole Proprietor Brand Registrations.

        Args:
            brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_brand_registration_otp(
            brand_registration_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1BrandRegistrationOtpWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1BrandRegistrationOtp:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1BrandRegistrationOtpWithRawResponse(client, server, auth)

    async def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrationsBrandRegistrationOtp:
        """A Messaging Service resource to retry OTP verification for Sole Proprietor Brand Registrations.

        Args:
            brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_brand_registration_otp(
                brand_registration_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1BrandRegistrationOtpWithRawResponse:
        return self._with_raw_response


class MessagingV1BrandRegistrationOtpWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandRegistrationOtp, RawError]:
        """A Messaging Service resource to retry OTP verification for Sole Proprietor Brand Registrations.

        Args:
            brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandRegistrationSid}/SmsOtp"),
            path_params=[param[str]("BrandRegistrationSid", brand_registration_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandRegistrationOtp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1BrandRegistrationOtpWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandRegistrationOtp, RawError]:
        """A Messaging Service resource to retry OTP verification for Sole Proprietor Brand Registrations.

        Args:
            brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandRegistrationSid}/SmsOtp"),
            path_params=[param[str]("BrandRegistrationSid", brand_registration_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandRegistrationOtp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
