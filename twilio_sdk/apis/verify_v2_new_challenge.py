from __future__ import annotations

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
from ..models.create_passkeys_challenge_request import (
    CreatePasskeysChallengeRequest,
    CreatePasskeysChallengeRequestDict,
)
from ..models.v2_services_passkeys_challenges_response import V2ServicesPasskeysChallengesResponse
from ..server.server import Server


class VerifyV2NewChallenge:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2NewChallengeWithRawResponse(client, server, auth)

    def create_challenge_passkeys(
        self,
        service_sid: str,
        body: CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ServicesPasskeysChallengesResponse:
        """Create a Passkeys Challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_challenge_passkeys(
            service_sid, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2NewChallengeWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2NewChallenge:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2NewChallengeWithRawResponse(client, server, auth)

    async def create_challenge_passkeys(
        self,
        service_sid: str,
        body: CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ServicesPasskeysChallengesResponse:
        """Create a Passkeys Challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_challenge_passkeys(service_sid, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2NewChallengeWithRawResponse:
        return self._with_raw_response


class VerifyV2NewChallengeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_challenge_passkeys(
        self,
        service_sid: str,
        body: CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ServicesPasskeysChallengesResponse, RawError]:
        """Create a Passkeys Challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/Challenges"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=json_body[CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysChallengesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2NewChallengeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_challenge_passkeys(
        self,
        service_sid: str,
        body: CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ServicesPasskeysChallengesResponse, RawError]:
        """Create a Passkeys Challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/Challenges"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=json_body[CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysChallengesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
