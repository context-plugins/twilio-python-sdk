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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.content_create_request import ContentCreateRequest, ContentCreateRequestDict
from ..models.content_update_request import ContentUpdateRequest, ContentUpdateRequestDict
from ..models.content_v1_content import ContentV1Content
from ..models.list_content_response import ListContentResponse
from ..server.server import Server


class Contentv1ContentApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Contentv1ContentApiWithRawResponse(client, server, auth)

    def create_content(
        self,
        body: ContentCreateRequest | ContentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1Content:
        """Create a Content resource

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_content(body, request_options=request_options).unwrap()

    def delete_content(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_content(sid, request_options=request_options).unwrap()

    def fetch_content(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ContentV1Content:
        """Fetch a Content resource by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_content(sid, request_options=request_options).unwrap()

    def list_content(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListContentResponse:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_content(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_content(
        self,
        sid: str,
        body: ContentUpdateRequest | ContentUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1Content:
        """Update a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_content(sid, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> Contentv1ContentApiWithRawResponse:
        return self._with_raw_response


class AsyncContentv1ContentApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncContentv1ContentApiWithRawResponse(client, server, auth)

    async def create_content(
        self,
        body: ContentCreateRequest | ContentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1Content:
        """Create a Content resource

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_content(body, request_options=request_options)).unwrap()

    async def delete_content(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_content(sid, request_options=request_options)).unwrap()

    async def fetch_content(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ContentV1Content:
        """Fetch a Content resource by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_content(sid, request_options=request_options)).unwrap()

    async def list_content(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListContentResponse:
        """Retrieve a list of Contents belonging to the account used to make the request

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
            await self._with_raw_response.list_content(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_content(
        self,
        sid: str,
        body: ContentUpdateRequest | ContentUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1Content:
        """Update a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_content(sid, body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncContentv1ContentApiWithRawResponse:
        return self._with_raw_response


class Contentv1ContentApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_content(
        self,
        body: ContentCreateRequest | ContentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1Content, RawError]:
        """Create a Content resource

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/v1/Content"),
            body=json_body[ContentCreateRequest | ContentCreateRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_content(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_content(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentV1Content, RawError]:
        """Fetch a Content resource by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_content(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListContentResponse, RawError]:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListContentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_content(
        self,
        sid: str,
        body: ContentUpdateRequest | ContentUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1Content, RawError]:
        """Update a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=json_body[ContentUpdateRequest | ContentUpdateRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncContentv1ContentApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_content(
        self,
        body: ContentCreateRequest | ContentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1Content, RawError]:
        """Create a Content resource

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/v1/Content"),
            body=json_body[ContentCreateRequest | ContentCreateRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_content(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_content(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentV1Content, RawError]:
        """Fetch a Content resource by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_content(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListContentResponse, RawError]:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListContentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_content(
        self,
        sid: str,
        body: ContentUpdateRequest | ContentUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1Content, RawError]:
        """Update a Content resource

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default2("/v1/Content/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=json_body[ContentUpdateRequest | ContentUpdateRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1Content],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
