from __future__ import annotations

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
from ..models.messaging_v1_external_campaign import MessagingV1ExternalCampaign
from ..server.server import Server


class MessagingV1ExternalCampaignApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1ExternalCampaignApiWithRawResponse(client, server, auth)

    def create_external_campaign(
        self,
        campaign_id: str,
        messaging_service_sid: str,
        *,
        cnp_migration: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ExternalCampaign:
        """Resource to associate preregistered campaign with Messaging Service.

        Args:
            campaign_id: ID of the preregistered campaign.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the resource is associated with.
            cnp_migration: Customers should use this flag during the ERC registration process to indicate to Twilio that
                the campaign being registered is undergoing CNP migration. It is important for the user to first trigger
                the CNP migration process for said campaign in their CSP portal and have Twilio accept the sharing
                request, before making this api call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_external_campaign(
            campaign_id, messaging_service_sid, cnp_migration=cnp_migration, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1ExternalCampaignApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1ExternalCampaignApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1ExternalCampaignApiWithRawResponse(client, server, auth)

    async def create_external_campaign(
        self,
        campaign_id: str,
        messaging_service_sid: str,
        *,
        cnp_migration: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ExternalCampaign:
        """Resource to associate preregistered campaign with Messaging Service.

        Args:
            campaign_id: ID of the preregistered campaign.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the resource is associated with.
            cnp_migration: Customers should use this flag during the ERC registration process to indicate to Twilio that
                the campaign being registered is undergoing CNP migration. It is important for the user to first trigger
                the CNP migration process for said campaign in their CSP portal and have Twilio accept the sharing
                request, before making this api call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_external_campaign(
                campaign_id, messaging_service_sid, cnp_migration=cnp_migration, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1ExternalCampaignApiWithRawResponse:
        return self._with_raw_response


class MessagingV1ExternalCampaignApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_external_campaign(
        self,
        campaign_id: str,
        messaging_service_sid: str,
        *,
        cnp_migration: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ExternalCampaign, RawError]:
        """Resource to associate preregistered campaign with Messaging Service.

        Args:
            campaign_id: ID of the preregistered campaign.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the resource is associated with.
            cnp_migration: Customers should use this flag during the ERC registration process to indicate to Twilio that
                the campaign being registered is undergoing CNP migration. It is important for the user to first trigger
                the CNP migration process for said campaign in their CSP portal and have Twilio accept the sharing
                request, before making this api call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/PreregisteredUsa2p"),
            body=form_body(
                [
                    param[str]("CampaignId", campaign_id),
                    param[str]("MessagingServiceSid", messaging_service_sid),
                    param[bool | None]("CnpMigration", cnp_migration),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ExternalCampaign],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1ExternalCampaignApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_external_campaign(
        self,
        campaign_id: str,
        messaging_service_sid: str,
        *,
        cnp_migration: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ExternalCampaign, RawError]:
        """Resource to associate preregistered campaign with Messaging Service.

        Args:
            campaign_id: ID of the preregistered campaign.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the resource is associated with.
            cnp_migration: Customers should use this flag during the ERC registration process to indicate to Twilio that
                the campaign being registered is undergoing CNP migration. It is important for the user to first trigger
                the CNP migration process for said campaign in their CSP portal and have Twilio accept the sharing
                request, before making this api call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/PreregisteredUsa2p"),
            body=form_body(
                [
                    param[str]("CampaignId", campaign_id),
                    param[str]("MessagingServiceSid", messaging_service_sid),
                    param[bool | None]("CnpMigration", cnp_migration),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ExternalCampaign],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
