from __future__ import annotations

from uuid import UUID, uuid4

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
from ..models.enums.brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProviderOrStr
from ..models.list_brand_vetting_response import ListBrandVettingResponse
from ..models.messaging_v1_brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting
from ..server.server import Server


class MessagingV1BrandVetting:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1BrandVettingWithRawResponse(client, server, auth)

    def create_brand_vetting(
        self,
        brand_sid: str,
        vetting_provider: BrandVettingEnumVettingProviderOrStr,
        *,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to create .
            vetting_provider: The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign
                Verify tokens) or “AEGIS” (Secondary Vetting).
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_brand_vetting(
            brand_sid, vetting_provider, vetting_id=vetting_id, request_options=request_options
        ).unwrap()

    def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            brand_vetting_sid: The Twilio SID of the third-party vetting record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_brand_vetting(
            brand_sid, brand_vetting_sid, request_options=request_options
        ).unwrap()

    def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProviderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBrandVettingResponse:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            vetting_provider: The third-party provider of the vettings to read
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_brand_vetting(
            brand_sid, vetting_provider=vetting_provider, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1BrandVettingWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1BrandVetting:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1BrandVettingWithRawResponse(client, server, auth)

    async def create_brand_vetting(
        self,
        brand_sid: str,
        vetting_provider: BrandVettingEnumVettingProviderOrStr,
        *,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to create .
            vetting_provider: The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign
                Verify tokens) or “AEGIS” (Secondary Vetting).
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_brand_vetting(
                brand_sid, vetting_provider, vetting_id=vetting_id, request_options=request_options
            )
        ).unwrap()

    async def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            brand_vetting_sid: The Twilio SID of the third-party vetting record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_brand_vetting(
                brand_sid, brand_vetting_sid, request_options=request_options
            )
        ).unwrap()

    async def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProviderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBrandVettingResponse:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            vetting_provider: The third-party provider of the vettings to read
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_brand_vetting(
                brand_sid, vetting_provider=vetting_provider, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1BrandVettingWithRawResponse:
        return self._with_raw_response


class MessagingV1BrandVettingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_brand_vetting(
        self,
        brand_sid: str,
        vetting_provider: BrandVettingEnumVettingProviderOrStr,
        *,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to create .
            vetting_provider: The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign
                Verify tokens) or “AEGIS” (Secondary Vetting).
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings"),
            path_params=[param[str]("BrandSid", brand_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[BrandVettingEnumVettingProviderOrStr]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandVetting],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            brand_vetting_sid: The Twilio SID of the third-party vetting record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid}"),
            path_params=[param[str]("BrandSid", brand_sid), param[str]("BrandVettingSid", brand_vetting_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandVetting],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProviderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBrandVettingResponse, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            vetting_provider: The third-party provider of the vettings to read
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings"),
            path_params=[param[str]("BrandSid", brand_sid)],
            query_params=[param[BrandVettingEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBrandVettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1BrandVettingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_brand_vetting(
        self,
        brand_sid: str,
        vetting_provider: BrandVettingEnumVettingProviderOrStr,
        *,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to create .
            vetting_provider: The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign
                Verify tokens) or “AEGIS” (Secondary Vetting).
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings"),
            path_params=[param[str]("BrandSid", brand_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[BrandVettingEnumVettingProviderOrStr]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandVetting],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            brand_vetting_sid: The Twilio SID of the third-party vetting record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid}"),
            path_params=[param[str]("BrandSid", brand_sid), param[str]("BrandVettingSid", brand_vetting_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrationsBrandVetting],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProviderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBrandVettingResponse, RawError]:
        """A Messaging Service resource to add and get Brand Vettings.

        Args:
            brand_sid: The SID of the Brand Registration resource of the vettings to read .
            vetting_provider: The third-party provider of the vettings to read
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{BrandSid}/Vettings"),
            path_params=[param[str]("BrandSid", brand_sid)],
            query_params=[param[BrandVettingEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBrandVettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
