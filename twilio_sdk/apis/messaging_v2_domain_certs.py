from __future__ import annotations

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
from ..models.messaging_v2_domain_cert_v4 import MessagingV2DomainCertV4
from ..server.server import Server


class MessagingV2DomainCerts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV2DomainCertsWithRawResponse(client, server, auth)

    def fetch_domain_cert_v42(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV2DomainCertV4:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_domain_cert_v42(domain_sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV2DomainCertsWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV2DomainCerts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV2DomainCertsWithRawResponse(client, server, auth)

    async def fetch_domain_cert_v42(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV2DomainCertV4:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_domain_cert_v42(domain_sid, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV2DomainCertsWithRawResponse:
        return self._with_raw_response


class MessagingV2DomainCertsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_domain_cert_v42(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV2DomainCertV4, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV2DomainCertsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_domain_cert_v42(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV2DomainCertV4, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
