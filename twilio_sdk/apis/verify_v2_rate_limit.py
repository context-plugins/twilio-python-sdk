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
from ..models.list_rate_limit_response import ListRateLimitResponse
from ..models.verify_v2_service_rate_limit import VerifyV2ServiceRateLimit
from ..server.server import Server


class VerifyV2RateLimit:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2RateLimitWithRawResponse(client, server, auth)

    def create_rate_limit(
        self,
        service_sid: str,
        unique_name: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimit:
        """Create a new Rate Limit for a Service

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the
                developer, to be optionally used in addition to SID. **This value should not contain PII.**
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_rate_limit(
            service_sid, unique_name, description=description, request_options=request_options
        ).unwrap()

    def delete_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_rate_limit(service_sid, sid, request_options=request_options).unwrap()

    def fetch_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceRateLimit:
        """Fetch a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_rate_limit(service_sid, sid, request_options=request_options).unwrap()

    def list_rate_limit(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRateLimitResponse:
        """Retrieve a list of all Rate Limits for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_rate_limit(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_rate_limit(
        self,
        service_sid: str,
        sid: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimit:
        """Update a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_rate_limit(
            service_sid, sid, description=description, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2RateLimitWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2RateLimit:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2RateLimitWithRawResponse(client, server, auth)

    async def create_rate_limit(
        self,
        service_sid: str,
        unique_name: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimit:
        """Create a new Rate Limit for a Service

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the
                developer, to be optionally used in addition to SID. **This value should not contain PII.**
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_rate_limit(
                service_sid, unique_name, description=description, request_options=request_options
            )
        ).unwrap()

    async def delete_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_rate_limit(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceRateLimit:
        """Fetch a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_rate_limit(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_rate_limit(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRateLimitResponse:
        """Retrieve a list of all Rate Limits for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_rate_limit(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_rate_limit(
        self,
        service_sid: str,
        sid: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimit:
        """Update a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_rate_limit(
                service_sid, sid, description=description, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2RateLimitWithRawResponse:
        return self._with_raw_response


class VerifyV2RateLimitWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_rate_limit(
        self,
        service_sid: str,
        unique_name: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Create a new Rate Limit for a Service

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the
                developer, to be optionally used in addition to SID. **This value should not contain PII.**
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("UniqueName", unique_name), param[str | None]("Description", description)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Fetch a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_rate_limit(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRateLimitResponse, RawError]:
        """Retrieve a list of all Rate Limits for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRateLimitResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_rate_limit(
        self,
        service_sid: str,
        sid: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Update a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Description", description)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2RateLimitWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_rate_limit(
        self,
        service_sid: str,
        unique_name: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Create a new Rate Limit for a Service

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the
                developer, to be optionally used in addition to SID. **This value should not contain PII.**
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("UniqueName", unique_name), param[str | None]("Description", description)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_rate_limit(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Fetch a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_rate_limit(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRateLimitResponse, RawError]:
        """Retrieve a list of all Rate Limits for a service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRateLimitResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_rate_limit(
        self,
        service_sid: str,
        sid: str,
        *,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimit, RawError]:
        """Update a specific Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
            description: Description of this Rate Limit
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Description", description)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimit],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
