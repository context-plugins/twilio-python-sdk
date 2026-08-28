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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.messaging_v1_linkshortening_messaging_service import MessagingV1LinkshorteningMessagingService
from ..server.server import Server


class MessagingV1LinkshorteningMessagingServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1LinkshorteningMessagingServiceApiWithRawResponse(client, server, auth)

    def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1LinkshorteningMessagingService:
        """Send a ``POST`` request.

        Args:
            domain_sid: The domain SID to associate with a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to associate with a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        ).unwrap()

    def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1LinkshorteningMessagingServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1LinkshorteningMessagingServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1LinkshorteningMessagingServiceApiWithRawResponse(client, server, auth)

    async def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1LinkshorteningMessagingService:
        """Send a ``POST`` request.

        Args:
            domain_sid: The domain SID to associate with a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to associate with a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_linkshortening_messaging_service(
                domain_sid, messaging_service_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_linkshortening_messaging_service(
                domain_sid, messaging_service_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1LinkshorteningMessagingServiceApiWithRawResponse:
        return self._with_raw_response


class MessagingV1LinkshorteningMessagingServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1LinkshorteningMessagingService, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: The domain SID to associate with a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to associate with a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}"
            ),
            path_params=[param[str]("DomainSid", domain_sid), param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1LinkshorteningMessagingService],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1(
                "/v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}"
            ),
            path_params=[param[str]("DomainSid", domain_sid), param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1LinkshorteningMessagingServiceApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1LinkshorteningMessagingService, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: The domain SID to associate with a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to associate with a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}"
            ),
            path_params=[param[str]("DomainSid", domain_sid), param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1LinkshorteningMessagingService],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in
                messages sent with the associated messaging service will be shortened to the provided domain
            messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled,
                links in messages sent with the provided messaging service will be shortened to the associated domain
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1(
                "/v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}"
            ),
            path_params=[param[str]("DomainSid", domain_sid), param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
