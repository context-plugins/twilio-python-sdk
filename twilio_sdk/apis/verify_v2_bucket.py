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
from ..models.list_bucket_response import ListBucketResponse
from ..models.verify_v2_service_rate_limit_bucket import VerifyV2ServiceRateLimitBucket
from ..server.server import Server


class VerifyV2Bucket:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2BucketWithRawResponse(client, server, auth)

    def create_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        max: int,
        interval: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimitBucket:
        """Create a new Bucket for a Rate Limit

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bucket(
            service_sid, rate_limit_sid, max, interval, request_options=request_options
        ).unwrap()

    def delete_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_bucket(
            service_sid, rate_limit_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceRateLimitBucket:
        """Fetch a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_bucket(
            service_sid, rate_limit_sid, sid, request_options=request_options
        ).unwrap()

    def list_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBucketResponse:
        """Retrieve a list of all Buckets for a Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_bucket(
            service_sid,
            rate_limit_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        sid: str,
        *,
        max: int | None = None,
        interval: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimitBucket:
        """Update a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_bucket(
            service_sid, rate_limit_sid, sid, max=max, interval=interval, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2BucketWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2Bucket:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2BucketWithRawResponse(client, server, auth)

    async def create_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        max: int,
        interval: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimitBucket:
        """Create a new Bucket for a Rate Limit

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_bucket(
                service_sid, rate_limit_sid, max, interval, request_options=request_options
            )
        ).unwrap()

    async def delete_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_bucket(
                service_sid, rate_limit_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceRateLimitBucket:
        """Fetch a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_bucket(
                service_sid, rate_limit_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBucketResponse:
        """Retrieve a list of all Buckets for a Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_bucket(
                service_sid,
                rate_limit_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        sid: str,
        *,
        max: int | None = None,
        interval: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceRateLimitBucket:
        """Update a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_bucket(
                service_sid, rate_limit_sid, sid, max=max, interval=interval, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2BucketWithRawResponse:
        return self._with_raw_response


class VerifyV2BucketWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        max: int,
        interval: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Create a new Bucket for a Rate Limit

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("RateLimitSid", rate_limit_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[int]("Max", max), param[int]("Interval", interval)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Fetch a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBucketResponse, RawError]:
        """Retrieve a list of all Buckets for a Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("RateLimitSid", rate_limit_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBucketResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        sid: str,
        *,
        max: int | None = None,
        interval: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Update a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[int | None]("Max", max), param[int | None]("Interval", interval)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2BucketWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        max: int,
        interval: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Create a new Bucket for a Rate Limit

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("RateLimitSid", rate_limit_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[int]("Max", max), param[int]("Interval", interval)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_bucket(
        self, service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Fetch a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBucketResponse, RawError]:
        """Retrieve a list of all Buckets for a Rate Limit.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("RateLimitSid", rate_limit_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBucketResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_bucket(
        self,
        service_sid: str,
        rate_limit_sid: str,
        sid: str,
        *,
        max: int | None = None,
        interval: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceRateLimitBucket, RawError]:
        """Update a specific Bucket.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is
                associated with.
            rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
            sid: A 34 character string that uniquely identifies this Bucket.
            max: Maximum number of requests permitted in during the interval.
            interval: Number of seconds that the rate limit will be enforced over.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("RateLimitSid", rate_limit_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[int | None]("Max", max), param[int | None]("Interval", interval)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceRateLimitBucket],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
