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
from ..models.messaging_v1_service_us_app_to_person_usecase import MessagingV1ServiceUsAppToPersonUsecase
from ..server.server import Server


class MessagingV1UsAppToPersonUsecase:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1UsAppToPersonUsecaseWithRawResponse(client, server, auth)

    def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonUsecase:
        """Messaging Service Use Case resource. Fetch possible use cases for service. The Use Cases API returns an empty
        list if there is an issue with the customer's A2P brand registration. This Brand cannot register any campaign
        use cases. Customers are requested to contact support with their A2P brand information.

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            brand_registration_sid: The unique string to identify the A2P brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_us_app_to_person_usecase(
            messaging_service_sid, brand_registration_sid=brand_registration_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1UsAppToPersonUsecaseWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1UsAppToPersonUsecase:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1UsAppToPersonUsecaseWithRawResponse(client, server, auth)

    async def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonUsecase:
        """Messaging Service Use Case resource. Fetch possible use cases for service. The Use Cases API returns an empty
        list if there is an issue with the customer's A2P brand registration. This Brand cannot register any campaign
        use cases. Customers are requested to contact support with their A2P brand information.

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            brand_registration_sid: The unique string to identify the A2P brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_us_app_to_person_usecase(
                messaging_service_sid, brand_registration_sid=brand_registration_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1UsAppToPersonUsecaseWithRawResponse:
        return self._with_raw_response


class MessagingV1UsAppToPersonUsecaseWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonUsecase, RawError]:
        """Messaging Service Use Case resource. Fetch possible use cases for service. The Use Cases API returns an empty
        list if there is an issue with the customer's A2P brand registration. This Brand cannot register any campaign
        use cases. Customers are requested to contact support with their A2P brand information.

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            brand_registration_sid: The unique string to identify the A2P brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[param[str | None]("BrandRegistrationSid", brand_registration_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonUsecase],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1UsAppToPersonUsecaseWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonUsecase, RawError]:
        """Messaging Service Use Case resource. Fetch possible use cases for service. The Use Cases API returns an empty
        list if there is an issue with the customer's A2P brand registration. This Brand cannot register any campaign
        use cases. Customers are requested to contact support with their A2P brand information.

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            brand_registration_sid: The unique string to identify the A2P brand.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[param[str | None]("BrandRegistrationSid", brand_registration_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonUsecase],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
