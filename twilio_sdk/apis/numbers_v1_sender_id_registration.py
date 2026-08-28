from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
)
from ..errors.create_sender_id_registration_error import (
    CreateSenderIdRegistrationErrorBody,
    create_sender_id_registration_error_mapper,
)
from ..models.numbers_v1_create_embedded_registration_request import (
    NumbersV1CreateEmbeddedRegistrationRequest,
    NumbersV1CreateEmbeddedRegistrationRequestDict,
)
from ..models.numbers_v1_create_embedded_registration_response import NumbersV1CreateEmbeddedRegistrationResponse
from ..server.server import Server


class NumbersV1SenderIdRegistration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1SenderIdRegistrationWithRawResponse(client, server, auth)

    def create_sender_id_registration(
        self,
        body: NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1CreateEmbeddedRegistrationResponse:
        """Creates a new sender ID registration and initializes an embedded Persona inquiry session. Returns
        registration details and embedded session credentials for rendering the Compliance Embeddable UI.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Internal Server Error ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return self._with_raw_response.create_sender_id_registration(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1SenderIdRegistrationWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1SenderIdRegistration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1SenderIdRegistrationWithRawResponse(client, server, auth)

    async def create_sender_id_registration(
        self,
        body: NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1CreateEmbeddedRegistrationResponse:
        """Creates a new sender ID registration and initializes an embedded Persona inquiry session. Returns
        registration details and embedded session credentials for rendering the Compliance Embeddable UI.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Internal Server Error ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return (
            await self._with_raw_response.create_sender_id_registration(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1SenderIdRegistrationWithRawResponse:
        return self._with_raw_response


class NumbersV1SenderIdRegistrationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sender_id_registration(
        self,
        body: NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1CreateEmbeddedRegistrationResponse, CreateSenderIdRegistrationErrorBody]:
        """Creates a new sender ID registration and initializes an embedded Persona inquiry session. Returns
        registration details and embedded session credentials for rendering the Compliance Embeddable UI.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SenderIdRegistrations"),
            body=json_body[NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1CreateEmbeddedRegistrationResponse],
            error_mapper=create_sender_id_registration_error_mapper,
            request_options=request_options,
        )


class AsyncNumbersV1SenderIdRegistrationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sender_id_registration(
        self,
        body: NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1CreateEmbeddedRegistrationResponse, CreateSenderIdRegistrationErrorBody]:
        """Creates a new sender ID registration and initializes an embedded Persona inquiry session. Returns
        registration details and embedded session credentials for rendering the Compliance Embeddable UI.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/SenderIdRegistrations"),
            body=json_body[NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1CreateEmbeddedRegistrationResponse],
            error_mapper=create_sender_id_registration_error_mapper,
            request_options=request_options,
        )
