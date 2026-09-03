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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_port_in_requests_response import ListPortInRequestsResponse
from ..models.numbers_v1_porting_port_in import NumbersV1PortingPortIn
from ..models.port_in_request import PortInRequest, PortInRequestDict
from ..server.server import Server


class NumbersV1PortingPortInApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingPortInApiWithRawResponse(client, server, auth)

    def create_porting_port_in(
        self, body: PortInRequest | PortInRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortIn:
        """Allows to create a new port in request

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_porting_port_in(body, request_options=request_options).unwrap()

    def delete_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Allows to cancel a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_porting_port_in(
            port_in_request_sid, request_options=request_options
        ).unwrap()

    def fetch_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortIn:
        """Fetch a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_porting_port_in(
            port_in_request_sid, request_options=request_options
        ).unwrap()

    def list_port_in_requests(
        self,
        *,
        token: str | None = None,
        size: int | None = 20,
        port_in_request_sid: str | None = None,
        port_in_request_status: str | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPortInRequestsResponse:
        """Retrieve a list of all PortInRequests for a user

        Args:
            token: Page start token, if null then it will start from the beginning
            size: Number of items per page
            port_in_request_sid: Filter by Port in request SID, supports multiple values separated by comma
            port_in_request_status: Filter by Port In request status
            created_before: Find all created before a certain date
            created_after: Find all created after a certain date
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_port_in_requests(
            token=token,
            size=size,
            port_in_request_sid=port_in_request_sid,
            port_in_request_status=port_in_request_status,
            created_before=created_before,
            created_after=created_after,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingPortInApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingPortInApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingPortInApiWithRawResponse(client, server, auth)

    async def create_porting_port_in(
        self, body: PortInRequest | PortInRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortIn:
        """Allows to create a new port in request

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_porting_port_in(body, request_options=request_options)).unwrap()

    async def delete_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Allows to cancel a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_porting_port_in(port_in_request_sid, request_options=request_options)
        ).unwrap()

    async def fetch_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortIn:
        """Fetch a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_porting_port_in(port_in_request_sid, request_options=request_options)
        ).unwrap()

    async def list_port_in_requests(
        self,
        *,
        token: str | None = None,
        size: int | None = 20,
        port_in_request_sid: str | None = None,
        port_in_request_status: str | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPortInRequestsResponse:
        """Retrieve a list of all PortInRequests for a user

        Args:
            token: Page start token, if null then it will start from the beginning
            size: Number of items per page
            port_in_request_sid: Filter by Port in request SID, supports multiple values separated by comma
            port_in_request_status: Filter by Port In request status
            created_before: Find all created before a certain date
            created_after: Find all created after a certain date
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_port_in_requests(
                token=token,
                size=size,
                port_in_request_sid=port_in_request_sid,
                port_in_request_status=port_in_request_status,
                created_before=created_before,
                created_after=created_after,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingPortInApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingPortInApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_porting_port_in(
        self, body: PortInRequest | PortInRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortIn, RawError]:
        """Allows to create a new port in request

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/Porting/PortIn"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PortInRequest | PortInRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortIn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Allows to cancel a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}"),
            path_params=[param[str]("PortInRequestSid", port_in_request_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortIn, RawError]:
        """Fetch a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}"),
            path_params=[param[str]("PortInRequestSid", port_in_request_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortIn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_port_in_requests(
        self,
        *,
        token: str | None = None,
        size: int | None = 20,
        port_in_request_sid: str | None = None,
        port_in_request_status: str | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPortInRequestsResponse, RawError]:
        """Retrieve a list of all PortInRequests for a user

        Args:
            token: Page start token, if null then it will start from the beginning
            size: Number of items per page
            port_in_request_sid: Filter by Port in request SID, supports multiple values separated by comma
            port_in_request_status: Filter by Port In request status
            created_before: Find all created before a certain date
            created_after: Find all created after a certain date
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/PortInRequests"),
            query_params=[
                param[str | None]("Token", token),
                param[int | None]("Size", size),
                param[str | None]("PortInRequestSid", port_in_request_sid),
                param[str | None]("PortInRequestStatus", port_in_request_status),
                param[str | None]("CreatedBefore", created_before),
                param[str | None]("CreatedAfter", created_after),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPortInRequestsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingPortInApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_porting_port_in(
        self, body: PortInRequest | PortInRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortIn, RawError]:
        """Allows to create a new port in request

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v1/Porting/PortIn"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PortInRequest | PortInRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortIn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Allows to cancel a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}"),
            path_params=[param[str]("PortInRequestSid", port_in_request_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_porting_port_in(
        self, port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortIn, RawError]:
        """Fetch a port in request by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}"),
            path_params=[param[str]("PortInRequestSid", port_in_request_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortIn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_port_in_requests(
        self,
        *,
        token: str | None = None,
        size: int | None = 20,
        port_in_request_sid: str | None = None,
        port_in_request_status: str | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPortInRequestsResponse, RawError]:
        """Retrieve a list of all PortInRequests for a user

        Args:
            token: Page start token, if null then it will start from the beginning
            size: Number of items per page
            port_in_request_sid: Filter by Port in request SID, supports multiple values separated by comma
            port_in_request_status: Filter by Port In request status
            created_before: Find all created before a certain date
            created_after: Find all created after a certain date
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/PortInRequests"),
            query_params=[
                param[str | None]("Token", token),
                param[int | None]("Size", size),
                param[str | None]("PortInRequestSid", port_in_request_sid),
                param[str | None]("PortInRequestStatus", port_in_request_status),
                param[str | None]("CreatedBefore", created_before),
                param[str | None]("CreatedAfter", created_after),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPortInRequestsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
