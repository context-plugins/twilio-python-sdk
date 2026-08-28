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
from ..models.list_brand_registrations_response import ListBrandRegistrationsResponse
from ..models.messaging_v1_brand_registrations import MessagingV1BrandRegistrations
from ..server.server import Server


class MessagingV1BrandRegistration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1BrandRegistrationWithRawResponse(client, server, auth)

    def create_brand_registrations(
        self,
        customer_profile_bundle_sid: str,
        a2_p_profile_bundle_sid: str,
        *,
        brand_type: str | None = None,
        mock: bool | None = None,
        skip_automatic_sec_vet: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            customer_profile_bundle_sid: Customer Profile Bundle Sid.
            a2_p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
            brand_type: Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low
                volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
            mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a
                mock brand. Defaults to false if no value is provided.
            skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be
                done.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_brand_registrations(
            customer_profile_bundle_sid,
            a2_p_profile_bundle_sid,
            brand_type=brand_type,
            mock=mock,
            skip_automatic_sec_vet=skip_automatic_sec_vet,
            request_options=request_options,
        ).unwrap()

    def fetch_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_brand_registrations(sid, request_options=request_options).unwrap()

    def list_brand_registrations(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBrandRegistrationsResponse:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_brand_registrations(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_brand_registrations(sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1BrandRegistrationWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1BrandRegistration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1BrandRegistrationWithRawResponse(client, server, auth)

    async def create_brand_registrations(
        self,
        customer_profile_bundle_sid: str,
        a2_p_profile_bundle_sid: str,
        *,
        brand_type: str | None = None,
        mock: bool | None = None,
        skip_automatic_sec_vet: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            customer_profile_bundle_sid: Customer Profile Bundle Sid.
            a2_p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
            brand_type: Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low
                volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
            mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a
                mock brand. Defaults to false if no value is provided.
            skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be
                done.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_brand_registrations(
                customer_profile_bundle_sid,
                a2_p_profile_bundle_sid,
                brand_type=brand_type,
                mock=mock,
                skip_automatic_sec_vet=skip_automatic_sec_vet,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_brand_registrations(sid, request_options=request_options)).unwrap()

    async def list_brand_registrations(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBrandRegistrationsResponse:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_brand_registrations(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1BrandRegistrations:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_brand_registrations(sid, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1BrandRegistrationWithRawResponse:
        return self._with_raw_response


class MessagingV1BrandRegistrationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_brand_registrations(
        self,
        customer_profile_bundle_sid: str,
        a2_p_profile_bundle_sid: str,
        *,
        brand_type: str | None = None,
        mock: bool | None = None,
        skip_automatic_sec_vet: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            customer_profile_bundle_sid: Customer Profile Bundle Sid.
            a2_p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
            brand_type: Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low
                volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
            mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a
                mock brand. Defaults to false if no value is provided.
            skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be
                done.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations"),
            body=form_body(
                [
                    param[str]("CustomerProfileBundleSid", customer_profile_bundle_sid),
                    param[str]("A2PProfileBundleSid", a2_p_profile_bundle_sid),
                    param[str | None]("BrandType", brand_type),
                    param[bool | None]("Mock", mock),
                    param[bool | None]("SkipAutomaticSecVet", skip_automatic_sec_vet),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_brand_registrations(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBrandRegistrationsResponse, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBrandRegistrationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1BrandRegistrationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_brand_registrations(
        self,
        customer_profile_bundle_sid: str,
        a2_p_profile_bundle_sid: str,
        *,
        brand_type: str | None = None,
        mock: bool | None = None,
        skip_automatic_sec_vet: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            customer_profile_bundle_sid: Customer Profile Bundle Sid.
            a2_p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
            brand_type: Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low
                volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
            mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a
                mock brand. Defaults to false if no value is provided.
            skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be
                done.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations"),
            body=form_body(
                [
                    param[str]("CustomerProfileBundleSid", customer_profile_bundle_sid),
                    param[str]("A2PProfileBundleSid", a2_p_profile_bundle_sid),
                    param[str | None]("BrandType", brand_type),
                    param[bool | None]("Mock", mock),
                    param[bool | None]("SkipAutomaticSecVet", skip_automatic_sec_vet),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_brand_registrations(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBrandRegistrationsResponse, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBrandRegistrationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_brand_registrations(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1BrandRegistrations, RawError]:
        """A Messaging Service resource to add and fetch Brand Registrations.

        Args:
            sid: The SID of the Brand Registration resource to update.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/a2p/BrandRegistrations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1BrandRegistrations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
