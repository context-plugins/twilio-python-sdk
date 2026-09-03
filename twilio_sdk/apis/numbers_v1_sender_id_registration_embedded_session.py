from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_sender_id_registration_embedded_session_error import (
    CreateSenderIdRegistrationEmbeddedSessionErrorBody,
    create_sender_id_registration_embedded_session_error_mapper,
)
from ..models.numbers_v1_create_embedded_session_request import (
    NumbersV1CreateEmbeddedSessionRequest,
    NumbersV1CreateEmbeddedSessionRequestDict,
)
from ..models.numbers_v1_create_embedded_session_response import NumbersV1CreateEmbeddedSessionResponse
from ..server.server import Server


class NumbersV1SenderIdRegistrationEmbeddedSession:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse(client, server, auth)

    def create_sender_id_registration_embedded_session(
        self,
        bundle_sid: str,
        body: NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1CreateEmbeddedSessionResponse:
        """Creates a new embedded Persona inquiry session for an existing registration in DRAFT or TWILIO_REJECTED
        status. Use this to resume an incomplete registration or resubmit a rejected one.

        Args:
            bundle_sid: The unique identifier of the registration (BU-prefixed).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict - Registration not in editable state Internal Server Error
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_sender_id_registration_embedded_session(
            bundle_sid, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1SenderIdRegistrationEmbeddedSession:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse(client, server, auth)

    async def create_sender_id_registration_embedded_session(
        self,
        bundle_sid: str,
        body: NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1CreateEmbeddedSessionResponse:
        """Creates a new embedded Persona inquiry session for an existing registration in DRAFT or TWILIO_REJECTED
        status. Use this to resume an incomplete registration or resubmit a rejected one.

        Args:
            bundle_sid: The unique identifier of the registration (BU-prefixed).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict - Registration not in editable state Internal Server Error
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_sender_id_registration_embedded_session(
                bundle_sid, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse:
        return self._with_raw_response


class NumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sender_id_registration_embedded_session(
        self,
        bundle_sid: str,
        body: NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1CreateEmbeddedSessionResponse, CreateSenderIdRegistrationEmbeddedSessionErrorBody]:
        """Creates a new embedded Persona inquiry session for an existing registration in DRAFT or TWILIO_REJECTED
        status. Use this to resume an incomplete registration or resubmit a rejected one.

        Args:
            bundle_sid: The unique identifier of the registration (BU-prefixed).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SenderIdRegistrations/{BundleSid}/EmbeddedSessions"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1CreateEmbeddedSessionResponse],
            error_mapper=create_sender_id_registration_embedded_session_error_mapper,
            request_options=request_options,
        )


class AsyncNumbersV1SenderIdRegistrationEmbeddedSessionWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_sender_id_registration_embedded_session(
        self,
        bundle_sid: str,
        body: NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1CreateEmbeddedSessionResponse, CreateSenderIdRegistrationEmbeddedSessionErrorBody]:
        """Creates a new embedded Persona inquiry session for an existing registration in DRAFT or TWILIO_REJECTED
        status. Use this to resume an incomplete registration or resubmit a rejected one.

        Args:
            bundle_sid: The unique identifier of the registration (BU-prefixed).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SenderIdRegistrations/{BundleSid}/EmbeddedSessions"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1CreateEmbeddedSessionResponse],
            error_mapper=create_sender_id_registration_embedded_session_error_mapper,
            request_options=request_options,
        )
