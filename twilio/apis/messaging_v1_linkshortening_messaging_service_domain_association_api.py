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
from ..models.messaging_v1_linkshortening_messaging_service_domain_association import (
    MessagingV1LinkshorteningMessagingServiceDomainAssociation,
)
from ..server.server import Server


class MessagingV1LinkshorteningMessagingServiceDomainAssociationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse(
            client, server, auth
        )

    def fetch_linkshortening_messaging_service_domain_association(
        self, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1LinkshorteningMessagingServiceDomainAssociation:
        """Send a ``GET`` request.

        Args:
            messaging_service_sid: Unique string used to identify the Messaging service that this domain should be
                associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_linkshortening_messaging_service_domain_association(
            messaging_service_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse(
            client, server, auth
        )

    async def fetch_linkshortening_messaging_service_domain_association(
        self, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1LinkshorteningMessagingServiceDomainAssociation:
        """Send a ``GET`` request.

        Args:
            messaging_service_sid: Unique string used to identify the Messaging service that this domain should be
                associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_linkshortening_messaging_service_domain_association(
                messaging_service_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse:
        return self._with_raw_response


class MessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse(
    SecuredRawResponse[RawClient, Server, AuthSchemes]
):
    def fetch_linkshortening_messaging_service_domain_association(
        self, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1LinkshorteningMessagingServiceDomainAssociation, RawError]:
        """Send a ``GET`` request.

        Args:
            messaging_service_sid: Unique string used to identify the Messaging service that this domain should be
                associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/MessagingServices/{MessagingServiceSid}/Domain"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1LinkshorteningMessagingServiceDomainAssociation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_linkshortening_messaging_service_domain_association(
        self, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1LinkshorteningMessagingServiceDomainAssociation, RawError]:
        """Send a ``GET`` request.

        Args:
            messaging_service_sid: Unique string used to identify the Messaging service that this domain should be
                associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/MessagingServices/{MessagingServiceSid}/Domain"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1LinkshorteningMessagingServiceDomainAssociation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
