from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.numbers_v1_eligibility import NumbersV1Eligibility
from ..server.server import Server


class NumbersV1EligibilityApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1EligibilityApiWithRawResponse(client, server, auth)

    def create_eligibility(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1Eligibility:
        """Create an eligibility check for a number that you want to host in Twilio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_eligibility(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1EligibilityApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1EligibilityApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1EligibilityApiWithRawResponse(client, server, auth)

    async def create_eligibility(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1Eligibility:
        """Create an eligibility check for a number that you want to host in Twilio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_eligibility(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1EligibilityApiWithRawResponse:
        return self._with_raw_response


class NumbersV1EligibilityApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_eligibility(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1Eligibility, RawError]:
        """Create an eligibility check for a number that you want to host in Twilio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/HostedNumber/Eligibility"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1Eligibility],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1EligibilityApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_eligibility(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1Eligibility, RawError]:
        """Create an eligibility check for a number that you want to host in Twilio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/HostedNumber/Eligibility"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1Eligibility],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
