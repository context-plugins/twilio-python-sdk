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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_service import ConversationsV1Service
from ..models.list_service_response2 import ListServiceResponse2
from ..server.server import Server


class ConversationsV1ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ServiceApiWithRawResponse(client, server, auth)

    def create_service3(
        self, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Service:
        """Create a new conversation service on your account

        Args:
            friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service3(friendly_name, request_options=request_options).unwrap()

    def delete_service3(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a conversation service with all its nested resources from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service3(sid, request_options=request_options).unwrap()

    def fetch_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Service:
        """Fetch a conversation service from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service3(sid, request_options=request_options).unwrap()

    def list_service3(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse2:
        """Retrieve a list of all conversation services on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service3(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1ServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ServiceApiWithRawResponse(client, server, auth)

    async def create_service3(
        self, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Service:
        """Create a new conversation service on your account

        Args:
            friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_service3(friendly_name, request_options=request_options)).unwrap()

    async def delete_service3(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a conversation service with all its nested resources from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_service3(sid, request_options=request_options)).unwrap()

    async def fetch_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Service:
        """Fetch a conversation service from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_service3(sid, request_options=request_options)).unwrap()

    async def list_service3(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse2:
        """Retrieve a list of all conversation services on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service3(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ServiceApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service3(
        self, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Service, RawError]:
        """Create a new conversation service on your account

        Args:
            friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services"),
            body=form_body([param[str]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a conversation service with all its nested resources from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Service, RawError]:
        """Fetch a conversation service from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service3(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse2, RawError]:
        """Retrieve a list of all conversation services on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service3(
        self, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Service, RawError]:
        """Create a new conversation service on your account

        Args:
            friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services"),
            body=form_body([param[str]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a conversation service with all its nested resources from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service3(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Service, RawError]:
        """Fetch a conversation service from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service3(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse2, RawError]:
        """Retrieve a list of all conversation services on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
