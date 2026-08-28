from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.messaging_v1_domain_cert_v4 import MessagingV1DomainCertV4
from ..server.server import Server


class MessagingV1DomainCerts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1DomainCertsWithRawResponse(client, server, auth)

    def delete_domain_cert_v4(self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_domain_cert_v4(domain_sid, request_options=request_options).unwrap()

    def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainCertV4:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_domain_cert_v4(domain_sid, request_options=request_options).unwrap()

    def update_domain_cert_v4(
        self, domain_sid: str, tls_cert: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainCertV4:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            tls_cert: Contains the full TLS certificate and private for this domain in PEM format:
                https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS
                traffic sent to your domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_domain_cert_v4(
            domain_sid, tls_cert, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1DomainCertsWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1DomainCerts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1DomainCertsWithRawResponse(client, server, auth)

    async def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_domain_cert_v4(domain_sid, request_options=request_options)
        ).unwrap()

    async def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainCertV4:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_domain_cert_v4(domain_sid, request_options=request_options)
        ).unwrap()

    async def update_domain_cert_v4(
        self, domain_sid: str, tls_cert: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainCertV4:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            tls_cert: Contains the full TLS certificate and private for this domain in PEM format:
                https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS
                traffic sent to your domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_domain_cert_v4(domain_sid, tls_cert, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1DomainCertsWithRawResponse:
        return self._with_raw_response


class MessagingV1DomainCertsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainCertV4, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_domain_cert_v4(
        self, domain_sid: str, tls_cert: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainCertV4, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            tls_cert: Contains the full TLS certificate and private for this domain in PEM format:
                https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS
                traffic sent to your domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("TlsCert", tls_cert)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1DomainCertsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainCertV4, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_domain_cert_v4(
        self, domain_sid: str, tls_cert: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainCertV4, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            tls_cert: Contains the full TLS certificate and private for this domain in PEM format:
                https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS
                traffic sent to your domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Certificate"),
            path_params=[param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("TlsCert", tls_cert)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainCertV4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
