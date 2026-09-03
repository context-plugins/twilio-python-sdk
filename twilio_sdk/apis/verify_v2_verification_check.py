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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.verify_v2_service_verification_check import VerifyV2ServiceVerificationCheck
from ..server.server import Server


class VerifyV2VerificationCheck:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2VerificationCheckWithRawResponse(client, server, auth)

    def create_verification_check(
        self,
        service_sid: str,
        *,
        code: str | None = None,
        to: str | None = None,
        verification_sid: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        sna_client_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerificationCheck:
        """challenge a specific Verification Check.

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            code: The 4-10 character string being verified.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Either this
                parameter or the ``verification_sid`` must be specified. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the ``to``
                phone number/`email <https://www.twilio.com/docs/verify/email>`__ must be specified.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            sna_client_token: A sna client token received in sna url invocation response needs to be passed in
                Verification Check request and should match to get successful response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_verification_check(
            service_sid,
            code=code,
            to=to,
            verification_sid=verification_sid,
            amount=amount,
            payee=payee,
            sna_client_token=sna_client_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2VerificationCheckWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2VerificationCheck:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2VerificationCheckWithRawResponse(client, server, auth)

    async def create_verification_check(
        self,
        service_sid: str,
        *,
        code: str | None = None,
        to: str | None = None,
        verification_sid: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        sna_client_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerificationCheck:
        """challenge a specific Verification Check.

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            code: The 4-10 character string being verified.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Either this
                parameter or the ``verification_sid`` must be specified. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the ``to``
                phone number/`email <https://www.twilio.com/docs/verify/email>`__ must be specified.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            sna_client_token: A sna client token received in sna url invocation response needs to be passed in
                Verification Check request and should match to get successful response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_verification_check(
                service_sid,
                code=code,
                to=to,
                verification_sid=verification_sid,
                amount=amount,
                payee=payee,
                sna_client_token=sna_client_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2VerificationCheckWithRawResponse:
        return self._with_raw_response


class VerifyV2VerificationCheckWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_verification_check(
        self,
        service_sid: str,
        *,
        code: str | None = None,
        to: str | None = None,
        verification_sid: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        sna_client_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerificationCheck, RawError]:
        """challenge a specific Verification Check.

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            code: The 4-10 character string being verified.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Either this
                parameter or the ``verification_sid`` must be specified. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the ``to``
                phone number/`email <https://www.twilio.com/docs/verify/email>`__ must be specified.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            sna_client_token: A sna client token received in sna url invocation response needs to be passed in
                Verification Check request and should match to get successful response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/VerificationCheck"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Code", code),
                    param[str | None]("To", to),
                    param[str | None]("VerificationSid", verification_sid),
                    param[str | None]("Amount", amount),
                    param[str | None]("Payee", payee),
                    param[str | None]("SnaClientToken", sna_client_token),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerificationCheck],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2VerificationCheckWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_verification_check(
        self,
        service_sid: str,
        *,
        code: str | None = None,
        to: str | None = None,
        verification_sid: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        sna_client_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerificationCheck, RawError]:
        """challenge a specific Verification Check.

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            code: The 4-10 character string being verified.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Either this
                parameter or the ``verification_sid`` must be specified. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the ``to``
                phone number/`email <https://www.twilio.com/docs/verify/email>`__ must be specified.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            sna_client_token: A sna client token received in sna url invocation response needs to be passed in
                Verification Check request and should match to get successful response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/VerificationCheck"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Code", code),
                    param[str | None]("To", to),
                    param[str | None]("VerificationSid", verification_sid),
                    param[str | None]("Amount", amount),
                    param[str | None]("Payee", payee),
                    param[str | None]("SnaClientToken", sna_client_token),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerificationCheck],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
