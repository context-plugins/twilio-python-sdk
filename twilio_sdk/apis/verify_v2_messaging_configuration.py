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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_messaging_configuration_response import ListMessagingConfigurationResponse
from ..models.verify_v2_service_messaging_configuration import VerifyV2ServiceMessagingConfiguration
from ..server.server import Server


class VerifyV2MessagingConfiguration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2MessagingConfigurationWithRawResponse(client, server, auth)

    def create_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Create a new MessagingConfiguration for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_messaging_configuration(
            service_sid, country, messaging_service_sid, request_options=request_options
        ).unwrap()

    def delete_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_messaging_configuration(
            service_sid, country, request_options=request_options
        ).unwrap()

    def fetch_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Fetch a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_messaging_configuration(
            service_sid, country, request_options=request_options
        ).unwrap()

    def list_messaging_configuration(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessagingConfigurationResponse:
        """Retrieve a list of all Messaging Configurations for a Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_messaging_configuration(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Update a specific MessagingConfiguration

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_messaging_configuration(
            service_sid, country, messaging_service_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2MessagingConfigurationWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2MessagingConfiguration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2MessagingConfigurationWithRawResponse(client, server, auth)

    async def create_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Create a new MessagingConfiguration for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_messaging_configuration(
                service_sid, country, messaging_service_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_messaging_configuration(
                service_sid, country, request_options=request_options
            )
        ).unwrap()

    async def fetch_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Fetch a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_messaging_configuration(
                service_sid, country, request_options=request_options
            )
        ).unwrap()

    async def list_messaging_configuration(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessagingConfigurationResponse:
        """Retrieve a list of all Messaging Configurations for a Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_messaging_configuration(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceMessagingConfiguration:
        """Update a specific MessagingConfiguration

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_messaging_configuration(
                service_sid, country, messaging_service_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2MessagingConfigurationWithRawResponse:
        return self._with_raw_response


class VerifyV2MessagingConfigurationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Create a new MessagingConfiguration for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Country", country), param[str]("MessagingServiceSid", messaging_service_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Fetch a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_messaging_configuration(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessagingConfigurationResponse, RawError]:
        """Retrieve a list of all Messaging Configurations for a Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessagingConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Update a specific MessagingConfiguration

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("MessagingServiceSid", messaging_service_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2MessagingConfigurationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Create a new MessagingConfiguration for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Country", country), param[str]("MessagingServiceSid", messaging_service_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_messaging_configuration(
        self, service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Fetch a specific MessagingConfiguration.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_messaging_configuration(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessagingConfigurationResponse, RawError]:
        """Retrieve a list of all Messaging Configurations for a Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessagingConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_messaging_configuration(
        self,
        service_sid: str,
        country: str,
        messaging_service_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]:
        """Update a specific MessagingConfiguration

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource
                is associated with.
            country: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country
                this configuration will be applied to. If this is a global configuration, Country will take the value
                ``all``.
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to send SMS to the country of
                this configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/MessagingConfigurations/{Country}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Country", country)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("MessagingServiceSid", messaging_service_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceMessagingConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
