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
from ..models.messaging_v1_request_managed_cert import MessagingV1RequestManagedCert
from ..server.server import Server


class MessagingV1RequestManagedCertApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1RequestManagedCertApiWithRawResponse(client, server, auth)

    def update_request_managed_cert(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1RequestManagedCert:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_request_managed_cert(domain_sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1RequestManagedCertApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1RequestManagedCertApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1RequestManagedCertApiWithRawResponse(client, server, auth)

    async def update_request_managed_cert(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1RequestManagedCert:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_request_managed_cert(domain_sid, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1RequestManagedCertApiWithRawResponse:
        return self._with_raw_response


class MessagingV1RequestManagedCertApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_request_managed_cert(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1RequestManagedCert, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/RequestManagedCert"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1RequestManagedCert],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1RequestManagedCertApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def update_request_managed_cert(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1RequestManagedCert, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this certificate should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/RequestManagedCert"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1RequestManagedCert],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
